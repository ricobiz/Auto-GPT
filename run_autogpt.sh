#!/bin/bash

echo "🚀 Запуск Auto-GPT с OpenRouter..."
echo "=================================="

# Активируем виртуальное окружение
source venv/bin/activate

# Запускаем Auto-GPT
python -m autogpt --gpt3only --skip-news

echo "Auto-GPT завершил работу."