#define SDL_MAIN_HANDLED
#include <vector>
#include <SDL.h>
#include <algorithm>
#include <iostream>
using namespace std;
const int TEXTURE_H = 2000;
const int TEXTURE_W = 2000;
const int SCREEN_H = 640;
const int SCREEN_W = 640;

int main()
{
    SDL_Rect source{0, 0, SCREEN_W / 4, SCREEN_H / 4}; //
    SDL_Rect dest{10, 10, SCREEN_W - 20, SCREEN_H - 20};
    SDL_Event e;
    SDL_Init(SDL_INIT_EVERYTHING);

    auto window = SDL_CreateWindow("Scrolling",
                                   SDL_WINDOWPOS_UNDEFINED,
                                   SDL_WINDOWPOS_UNDEFINED,
                                   SCREEN_W, SCREEN_H, 0);

    auto renderer = SDL_CreateRenderer(window, -1, 0);
    auto texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGBA8888, SDL_TEXTUREACCESS_TARGET,
                                     TEXTURE_W, TEXTURE_H);

    std::vector<SDL_Point> pv;
    for (int i = 0; i < 10000; i++)
    {
        pv.emplace_back(SDL_Point{rand() % TEXTURE_H, rand() % TEXTURE_W}); // 32k 767
    }
    auto running = true;
    while (running)
    {
        while (SDL_PollEvent(&e))
        {
            if (e.type == SDL_QUIT)
            {
                running = false;
            }
            if (e.type == SDL_KEYDOWN)
            {
                switch (e.key.keysym.sym)
                {
                case SDLK_UP:
                    source.y -= 3;
                    break;
                case SDLK_DOWN:
                    source.y += 3;
                    break;
                case SDLK_LEFT:
                    source.x -= 3;
                    break;
                case SDLK_RIGHT:
                    source.x += 3;
                    break;
                case SDLK_1:
                    source.w *= 2;
                    source.h *= 2;
                    break;
                case SDLK_2:
                    source.w /= 2;
                    source.h /= 2;
                    break;
                }
            }
            else if (e.type == SDL_MOUSEWHEEL)
            {
                if (e.wheel.y > 0)
                {
                    if (source.w * 2 <= TEXTURE_W && source.h * 2 <= TEXTURE_H)
                    {
                        source.w *= 2;
                        source.h *= 2;
                    }
                }
                else if (e.wheel.y < 0)
                {
                    if (source.h / 2 > 0 && source.w / 2 > 0)
                    {
                        source.h /= 2;
                        source.w /= 2;
                    }
                }
            }
            else if (e.type == SDL_MOUSEMOTION)
            {
                if (SDL_GetMouseState(nullptr, nullptr) & SDL_BUTTON(SDL_BUTTON_LEFT))
                {
                    source.x = std::min(TEXTURE_W - source.w, std::max(0, source.x + e.motion.xrel));
                    source.y = std::min(TEXTURE_H - source.h, std::max(0, source.y + e.motion.yrel));
                }
            }
        }
        // clear texture
        SDL_SetRenderTarget(renderer, texture);
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderClear(renderer);

        std::for_each(pv.begin(), pv.end(), [](auto &item)
                      {
            item.x += rand() % 3 - 1 ;
            item.y += rand() % 3 - 1; });
        std::cout << rand << endl;

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderDrawPoints(renderer, pv.data(), pv.size());

        SDL_SetRenderTarget(renderer, nullptr);
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, texture, &source, &dest);
        SDL_RenderPresent(renderer);

        SDL_Delay(50);
    }
    return 0;
}
