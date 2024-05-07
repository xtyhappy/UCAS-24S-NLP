import os
import math
import matplotlib.pyplot as plt

def read_text(file_path, size=None):
    with open(file_path, 'r', encoding='utf8') as file:
        return file.read(size).upper()  # 确保文本全为大写

def calculate_frequency(text):
    freq_dict = {}
    for char in text:
        if char.isalpha():  # 确保仅统计字母
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict

def calculate_entropy(freq_dict, total_chars):
    entropy = 0
    for freq in freq_dict.values():
        probability = freq / total_chars
        entropy -= probability * math.log2(probability)
    return entropy

def main():
    file_path = '/Users/amber/Desktop/2024spring/nlp/hw1/data/en_data/total_en.txt'
    result = []

    # 样本大小从0.5M开始，每次增加0.5M，直到10M
    sizes = [500_000 * (i + 1) for i in range(20)]

    for size in sizes:
        text = read_text(file_path, size)
        freq_dict = calculate_frequency(text)
        total_chars = sum(freq_dict.values())
        entropy = calculate_entropy(freq_dict, total_chars)
        top_chars = sorted(freq_dict, key=freq_dict.get, reverse=True)[:10]

        result.append({
            'size': size,
            'entropy': entropy,
            'top_chars': top_chars,
            'frequencies': [freq_dict[char] for char in top_chars]
        })

    return result

def plot_entropy(analysis_result):
    sizes = [entry['size'] for entry in analysis_result]
    entropies = [entry['entropy'] for entry in analysis_result]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, entropies, marker='o')
    plt.title("English Entropy Over Different Content Sizes")
    plt.xlabel("Content Size (bytes)")
    plt.ylabel("Entropy")
    plt.grid(True)
    plt.savefig('/Users/amber/Desktop/2024spring/nlp/hw1/result/en_entropy_chart.png')
    plt.close()

def write_results_to_file(analysis_result, file_path):
    with open(file_path, 'w', encoding='utf8') as file:
        for entry in analysis_result:
            file.write(f"Size: {entry['size']} bytes\n")
            file.write(f"Entropy: {entry['entropy']}\n")
            file.write("Top 10 Characters: " + ', '.join(entry['top_chars']) + "\n")
            file.write("Frequencies: " + ', '.join(map(str, entry['frequencies'])) + "\n\n")

# 运行程序并获取结果
analysis_result = main()
plot_entropy(analysis_result)

# 将结果写入文件
result_file_path = '/Users/amber/Desktop/2024spring/nlp/hw1/result/en.txt'
write_results_to_file(analysis_result, result_file_path)
