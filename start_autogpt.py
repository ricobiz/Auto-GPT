#!/usr/bin/env python3
"""
Скрипт для запуска AutoGPT
"""

import os
import sys

def main():
    print("🚀 Запуск Auto-GPT...")
    print("=" * 50)
    
    # Проверяем файл .env
    if not os.path.exists('.env'):
        print("❌ Файл .env не найден!")
        print("Скопируйте .env.template в .env и настройте OPENAI_API_KEY")
        return
    
    # Проверяем виртуальное окружение
    if not os.path.exists('venv'):
        print("❌ Виртуальное окружение не найдено!")
        print("Создайте его командой: python3 -m venv venv")
        return
    
    print("✅ Все готово к запуску!")
    print("📝 Для работы AutoGPT нужен настоящий OpenAI API ключ")
    print("🔧 Отредактируйте файл .env и укажите ваш OPENAI_API_KEY")
    print()
    print("🎯 Команды для запуска:")
    print("   source venv/bin/activate")
    print("   python -m autogpt --gpt3only --skip-news")
    print()
    print("📋 Или используйте готовый скрипт:")
    print("   ./run.sh")

if __name__ == "__main__":
    main()