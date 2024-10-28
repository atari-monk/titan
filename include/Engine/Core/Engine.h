#ifndef ENGINE_H
#define ENGINE_H

#include <memory>

class Engine {
public:
    Engine();
    ~Engine();

    void Init();
    void Run();
    void Shutdown();

private:
    bool isRunning;
    void Update();
    void Render();
};

#endif // ENGINE_H
