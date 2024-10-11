# job_alert/tasks.py
from celery import shared_task
from .models import Job, Profile
from django.core.mail import send_mail
from django.conf import settings
from fuzzywuzzy import fuzz 

import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup
from django.db import IntegrityError

#job matching and notification
@shared_task(bind=True)
def check_job_match_and_notify_users(self, job_id):
    print("inside celery task")
    try:
        job = Job.objects.get(id=job_id)
        # Fetch all profiles that match job criteria
        profiles = Profile.objects.filter(
            preferred_job_type=job.job_type
        )

        matched_profiles = []
        for profile in profiles:
            print(f"Job name({job_id}): {job.role.lower()}")
            if profile.preferred_job_location.lower() == "all india" or profile.preferred_job_location.lower() in job.location.lower() or job.location.lower() == 'india':
                match_score = fuzz.partial_ratio(profile.preferred_job_title.lower(), job.role.lower())
                print("match score:", match_score)
                if match_score > 60:
                    matched_profiles.append(profile)

        # Notify matched profiles
        for profile in matched_profiles:
            print("Insode mail loop")
            print(profile.user.email)
            send_mail(
                subject='New Job Matching Your Preferences!',
                message=f'Hi {profile.user.username},\n\nA new job "{job.role}" at {job.company_name} matches your preferences. Check it out: {job.link_to_original_source}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[profile.user.email],
                fail_silently=False,
            )

        print(f"Notifications sent to {len(matched_profiles)} users.")
    except Job.DoesNotExist:
        print("Job does not exist.")


#web scrapping
@shared_task(bind=True)
def scrape_jobs(self):
    urls = ["https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Industry&cboIndustry=28&pDate=Y&sequence=10&startPage=1",
            "https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Industry&cboIndustry=28&pDate=Y&sequence=7&startPage=1",
            "https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Industry&cboIndustry=28&pDate=Y&sequence=1&startPage=1", 
           "https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Industry&cboIndustry=28&pDate=Y&sequence=3&startPage=1",
           "https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Industry&cboIndustry=28&pDate=Y&sequence=4&startPage=1"]
    
    
    for url in urls:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        for job in jobs:
            try:
                role = job.find('h2').text.strip().split(',')[0].strip()
                company_name = job.find('h3', class_='joblist-comp-name').text.strip().split(',')[0].strip()
                location = job.find('ul', class_='top-jd-dtl clearfix').find('span').text.strip().split(',')[0]
                job_link = job.find('h2').a['href']
                job_detail_url = f"{job_link}"
                
                # Get job details like Employment Type
                job_detail_text = requests.get(job_detail_url).text
                job_detail_soup = BeautifulSoup(job_detail_text, 'lxml')
                employment_type = job_detail_soup.find('label', string="Employment Type:" ).next_sibling.strip()

                # Translate Employment Type to JOB_TYPE_CHOICES
                if employment_type.lower() == 'full time':
                    job_type = 'full_time'
                elif employment_type.lower() == 'part time':
                    job_type = 'part_time'
                else:
                    job_type = 'remote'

                # Add job to database if it's new
                if not Job.objects.filter(link_to_original_source=job_detail_url).exists():
                    Job.objects.create(
                        role=role,
                        company_name=company_name,
                        location=location,
                        link_to_original_source=job_detail_url,
                        job_type=job_type
                    )
                else:
                    print(f"Job {role} at {company_name} already exists.")

            except IntegrityError:
                # If a job with the same link already exists, skip
                print(f"Job {role} at {company_name} already exists.")
            except Exception as e:
                print(f"Error scraping job {role}: {str(e)}")
