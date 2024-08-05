# Исследование Looped Transformer'a (тестовое задание в LLM Foundations)
## Главное
Подробнее про эксперименты и анализ результатов можно почитать в файлике Analysis.ipynb. Скачать веса всех моделей, в нех упомянутом, можно [тут](https://disk.yandex.ru/d/Nth5Dcwy-y_ttw).
## Как воспроизвести
Создать среду и установить все необходимые библиотеки:
```sh
conda create --name <name>
conda activate <name>
pip install -r requirements.txt
```
Для запуска эксперимента необходимо отредактировать конфиг для обучения <code>configs/base_loop.yaml</code> и запустить обучение:
```sh
./exec/script_loop.sh
```
## Про код
Основные изменения по файлам:
- <code>scripts/models.py</code> - задачи 1/2/bonus, оформленные в качестве новых атрибутов к TransformerModelLooped
- <code>scripts/nano_gpt.py</code> - задачи 2/3 (SSM блок)
- <code>scripts/train.py</code> - добавлен репорт test loss'a на W&B
## Про эксперименты
Все эксперименты запускались с фиксированным рандом сидом на одной и той же GPU. Некоторые эксперименты повторялись несколько раз с разными сидами, чтобы убедиться в результате и сделать более точные выводы. <br />

Для отслеживания обучения использовался WandB (отчет по всем экспериментам можно найти [тут](https://api.wandb.ai/links/glinkamusic-ai/fsnu3hy6)). 

Основной конфиг для запуска обучения - <code>configs/base_loop.yaml</code>. Он основан на аналогичном конфиге из оригинального репозитория и редактируется под каждый конкретный эксперимент.
```yaml
wandb:
    project: Lets_Loop2
    notes:
    log_every_steps: 100

gpu:
    cuda: True

model:
    family: gpt2_loop
    n_embd: 256
    n_layer: 1
    n_head: 8
    n_dims: 20
    n_positions: 101
    save_n_tokens: 0
    feed_block: False
    use_ssm: False
    skip_connection: False

training:
    seed: 42 # 42 123 1233
    use_fixed_dataset: True
    test_every_steps: 10000
    test_size: 100000
    batch_size: 64
    task_name: linear_regression
    learning_rate: 0.0001
    weight_decay: 0.0
    train_steps: 100000
    save_every_steps: 1000
    keep_every_steps: 5000
    curriculum:
        dims:
            start: 5
            end: 20
            inc: 1
            interval: 5000
        points:
            start: 11
            end: 41
            inc: 2
            interval: 5000
        loops:
            start: 20
            end: 350
            inc: 2
            interval: 500
    n_loop_window: 20

out_dir: ./results2/linear_regression_loop
debug_mode: False
```
