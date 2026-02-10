import re
import os
import json

def extract_links_from_files(directory):
    link_pattern = re.compile(r"\[\[([^\]]+)\]\]")
    nodes = []
    links = []
    
    if not os.path.exists(directory):
        print(f"エラー: フォルダが見つかりません -> {directory}")
        return {"nodes": [], "links": []}

    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    
    for filename in files:
        source_id = os.path.splitext(filename)[0]
        nodes.append({"id": source_id, "group": 1})
        
        file_path = os.path.join(directory, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            found_links = link_pattern.findall(content)
            for target_id in found_links:
                links.append({"source": source_id, "target": target_id})
    
    return {"nodes": nodes, "links": links}

if __name__ == "__main__":
    # パスはあなたの環境に合わせています
    target_dir = r"E:\就労支援センター南\makeObsidian\python"
    graph_data = extract_links_from_files(target_dir)
    
    # 【重要】ここで data.json という名前で保存します
    # 保存先は pytest.py と同じフォルダになります
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2, ensure_ascii=False)
    
    print("成功！ data.json が作成されました。フォルダを確認してください。")