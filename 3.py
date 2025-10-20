import subprocess
import sys
import json
from graphviz import Digraph
import os
import matplotlib.pyplot as plt
import networkx as nx


def setup_graphviz_path():
    """Настройка пути к Graphviz"""
    graphviz_paths = [
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin",
        r"C:\Graphviz\bin"
    ]

    for path in graphviz_paths:
        if os.path.exists(path):
            os.environ["PATH"] += os.pathsep + path
            print(f"✓ Добавлен путь к Graphviz: {path}")
            return True
    return False


def create_matplotlib_networkx():
    """Создание графа matplotlib с помощью NetworkX"""
    G = nx.DiGraph()

    # Основной пакет
    G.add_node('matplotlib', color='lightcoral', size=3000)

    # Зависимости
    deps = ['numpy', 'pillow', 'cycler', 'kiwisolver', 'pyparsing',
            'python-dateutil', 'contourpy', 'fonttools', 'packaging']

    for dep in deps:
        G.add_node(dep, color='lightblue', size=2000)
        G.add_edge('matplotlib', dep)

    # Транзитивные зависимости
    G.add_node('six', color='lightgreen', size=1500)
    G.add_edge('python-dateutil', 'six')

    return G


def create_express_networkx():
    """Создание графа express с помощью NetworkX"""
    G = nx.DiGraph()

    # Основной пакет
    G.add_node('express', color='coral', size=3000)

    # Основные зависимости Express
    express_deps = ['body-parser', 'cookie', 'debug', 'accepts', 'path-to-regexp',
                    'qs', 'send', 'serve-static', 'finalhandler', 'http-errors']

    for dep in express_deps:
        G.add_node(dep, color='lightgreen', size=2000)
        G.add_edge('express', dep)

    return G


def draw_dependencies():
    """Отрисовка графов зависимостей"""
    plt.figure(figsize=(20, 10))

    # Граф matplotlib
    plt.subplot(1, 2, 1)
    G_matplotlib = create_matplotlib_networkx()

    pos = nx.spring_layout(G_matplotlib, k=2, iterations=50)
    colors = [G_matplotlib.nodes[node].get('color', 'lightblue') for node in G_matplotlib.nodes()]
    sizes = [G_matplotlib.nodes[node].get('size', 1500) for node in G_matplotlib.nodes()]

    nx.draw(G_matplotlib, pos, with_labels=True, node_color=colors,
            node_size=sizes, font_size=8, font_weight='bold',
            arrows=True, arrowsize=20, edge_color='gray')

    plt.title('Matplotlib Dependencies\n(Python Package)', fontsize=14, fontweight='bold')

    # Граф express
    plt.subplot(1, 2, 2)
    G_express = create_express_networkx()

    pos_express = nx.spring_layout(G_express, k=2, iterations=50)
    colors_express = [G_express.nodes[node].get('color', 'lightgreen') for node in G_express.nodes()]
    sizes_express = [G_express.nodes[node].get('size', 1500) for node in G_express.nodes()]

    nx.draw(G_express, pos_express, with_labels=True, node_color=colors_express,
            node_size=sizes_express, font_size=8, font_weight='bold',
            arrows=True, arrowsize=20, edge_color='gray')

    plt.title('Express Dependencies\n(JavaScript Package)', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('dependencies_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()


def create_detailed_matplotlib_graph():
    """Детальный граф зависимостей matplotlib"""
    dot = Digraph(comment='Matplotlib Dependencies')
    dot.attr(rankdir='TB')

    # Основной пакет
    dot.node('matplotlib', 'matplotlib', style='filled', fillcolor='lightcoral', shape='ellipse')

    # Основные зависимости
    main_deps = {
        'numpy': 'Численные вычисления',
        'pillow': 'Работа с изображениями',
        'cycler': 'Циклы стилей',
        'kiwisolver': 'Оптимизация layout',
        'pyparsing': 'Парсинг выражений',
        'python-dateutil': 'Работа с датами',
        'contourpy': 'Контурные графики',
        'fonttools': 'Работа со шрифтами',
        'packaging': 'Управление версиями'
    }

    for dep, description in main_deps.items():
        dot.node(dep, f'{dep}\n{description}', style='filled', fillcolor='lightblue')
        dot.edge('matplotlib', dep)

    # Транзитивные зависимости
    dot.node('six', 'six\nPython 2/3 совместимость', style='filled', fillcolor='lightgreen')
    dot.edge('python-dateutil', 'six')

    return dot


def main():
    """Основная функция"""
    print("Генерация графов зависимостей...")

    # Пытаемся настроить Graphviz
    if setup_graphviz_path():
        try:
            # Пробуем создать граф через Graphviz
            print("\n1. Пробуем создать граф через Graphviz...")
            matplotlib_graph = create_detailed_matplotlib_graph()
            matplotlib_graph.render('matplotlib_detailed', format='png', cleanup=True)
            print("✓ Детальный граф matplotlib создан через Graphviz")
        except Exception as e:
            print(f"Graphviz не сработал: {e}")

    # Создаем граф через NetworkX/Matplotlib
    print("\n2. Создаем граф через NetworkX/Matplotlib...")
    draw_dependencies()
    print("✓ Граф зависимостей сохранен как 'dependencies_comparison.png'")

    # Выводим информацию о зависимостях
    print("\n" + "=" * 50)
    print("ИНФОРМАЦИЯ О ЗАВИСИМОСТЯХ")
    print("=" * 50)

    print("\n📊 MATPLOTLIB (Python):")
    matplotlib_deps = ['numpy', 'pillow', 'cycler', 'kiwisolver', 'pyparsing',
                       'python-dateutil', 'contourpy', 'fonttools', 'packaging']
    for dep in matplotlib_deps:
        print(f"  • {dep}")

    print("\n🌐 EXPRESS (JavaScript):")
    express_deps = ['body-parser', 'cookie', 'debug', 'accepts', 'path-to-regexp',
                    'qs', 'send', 'serve-static', 'finalhandler', 'http-errors']
    for dep in express_deps:
        print(f"  • {dep}")


if __name__ == "__main__":
    main()