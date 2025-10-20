import click
import toml
import requests

config = {
    "package_name": "requests",
    "repo_url": "https://github.com/psf/requests",
    "test_repo_mode": "local",
    "version": "latest",
    "max_depth": 3,
    "filter_substring": ""
}


@click.command()
@click.option('--package', default=config['package_name'], help='Имя пакета для анализа')
@click.option('--repo', default=config['repo_url'], help='URL репозитория')
@click.option('--mode', default=config['test_repo_mode'], help='Режим работы (local/remote)')
@click.option('--version', default=config['version'], help='Версия пакета')
@click.option('--depth', default=config['max_depth'], help='Глубина анализа')
@click.option('--filter', default=config['filter_substring'], help='Фильтр пакетов')
def analyze(package, repo, mode, version, depth, filter):
    """Анализатор зависимостей пакетов"""
    print(f"Начало анализа пакета {package}")

    # Здесь будет логика анализа
    print("Анализ завершен!")

if __name__ == '__main__':
    analyze()