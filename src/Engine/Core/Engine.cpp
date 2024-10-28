#include "Engine/Core/Engine.h"
#include <iostream>

Engine::Engine() : isRunning(false) {}

Engine::~Engine() {
    Shutdown();
}

void Engine::Init() {
    std::cout << "Initializing Engine..." << std::endl;
    isRunning = true;
}

void Engine::Run() {
    while (isRunning) {
        Update();
        Render();
    }
}

void Engine::Shutdown() {
    std::cout << "Shutting down engine..." << std::endl;
}

void Engine::Update() {
    // Handle input, update game logic, etc.
    std::cout << "Updating..." << std::endl;
}

void Engine::Render() {
    // Render the scene
    std::cout << "Rendering..." << std::endl;
}
