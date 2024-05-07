import matplotlib.pyplot as plt

def plot_entropy(analysis_result):
    sizes = [entry['size'] for entry in analysis_result]
    entropies = [entry['entropy'] for entry in analysis_result]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, entropies, marker='o')
    plt.title("Chinese Entropy")
    plt.xlabel("Content Size")
    plt.ylabel("Entropy")
    plt.grid(True)
    plt.savefig('/Users/amber/Desktop/2024spring/nlp/hw1/result/entropy_chart.png')
    plt.close()

def plot_top_chars(analysis_result):
    top_chars = analysis_result[-1]['top_chars']  # 取最后一次分析的前10个字符
    frequencies = analysis_result[-1]['frequencies']

    plt.figure(figsize=(10, 6))
    plt.barh(top_chars, frequencies, color='skyblue')
    plt.title("Top 10 Chinese Characters Frequency")
    plt.xlabel("Frequency")
    plt.ylabel("Characters")
    plt.grid(True)
    plt.savefig('/Users/amber/Desktop/2024spring/nlp/hw1/result/top_chars_chart.png')
    plt.close()

# 从前一个脚本获取分析结果
# 假设 analysis_result 是从第一个脚本获取的数据

plot_entropy(analysis_result)
plot_top_chars(analysis_result)
