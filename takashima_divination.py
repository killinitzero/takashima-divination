import random
import sys
import time

# 八卦映射 (数字 -> 卦名)
TRIGRAMS = {
    1: {"name": "乾", "nature": "天"},
    2: {"name": "兑", "nature": "泽"},
    3: {"name": "离", "nature": "火"},
    4: {"name": "震", "nature": "雷"},
    5: {"name": "巽", "nature": "风"},
    6: {"name": "坎", "nature": "水"},
    7: {"name": "艮", "nature": "山"},
    8: {"name": "坤", "nature": "地"}
}

# 八卦对应的爻像 (从下到上, 0为阴, 1为阳)
TRIGRAM_LINES = {
    1: [1, 1, 1], # 乾
    2: [1, 1, 0], # 兑
    3: [1, 0, 1], # 离
    4: [1, 0, 0], # 震
    5: [0, 1, 1], # 巽
    6: [0, 1, 0], # 坎
    7: [0, 0, 1], # 艮
    8: [0, 0, 0]  # 坤
}

# 爻像反向映射 (爻像元组 -> 数字)
LINES_TO_TRIGRAM = {tuple(v): k for k, v in TRIGRAM_LINES.items()}

# 64卦全名映射 {(上卦, 下卦): "卦名"}
HEXAGRAM_NAMES = {
    (1, 1): "乾为天", (1, 2): "天泽履", (1, 3): "天火同人", (1, 4): "天雷无妄",
    (1, 5): "天风姤", (1, 6): "天水讼", (1, 7): "天山遁", (1, 8): "天地否",
    (2, 1): "泽天夬", (2, 2): "兑为泽", (2, 3): "泽火革", (2, 4): "泽雷随",
    (2, 5): "泽风大过", (2, 6): "泽水困", (2, 7): "泽山咸", (2, 8): "泽地萃",
    (3, 1): "火天大有", (3, 2): "火泽睽", (3, 3): "离为火", (3, 4): "火雷噬嗑",
    (3, 5): "火风鼎", (3, 6): "火水未济", (3, 7): "火山旅", (3, 8): "火地晋",
    (4, 1): "雷天大壮", (4, 2): "雷泽归妹", (4, 3): "雷火丰", (4, 4): "震为雷",
    (4, 5): "雷风恒", (4, 6): "雷水解", (4, 7): "雷山小过", (4, 8): "雷地豫",
    (5, 1): "风天小畜", (5, 2): "风泽中孚", (5, 3): "风火家人", (5, 4): "风雷益",
    (5, 5): "巽为风", (5, 6): "风水涣", (5, 7): "风山渐", (5, 8): "风地观",
    (6, 1): "水天需", (6, 2): "水泽节", (6, 3): "水火既济", (6, 4): "水雷屯",
    (6, 5): "水风井", (6, 6): "坎为水", (6, 7): "水山蹇", (6, 8): "水地比",
    (7, 1): "山天大畜", (7, 2): "山泽损", (7, 3): "山火贲", (7, 4): "山雷颐",
    (7, 5): "山风蛊", (7, 6): "山水蒙", (7, 7): "艮为山", (7, 8): "山地剥",
    (8, 1): "地天泰", (8, 2): "地泽临", (8, 3): "地火明夷", (8, 4): "地雷复",
    (8, 5): "地风升", (8, 6): "地水师", (8, 7): "地山谦", (8, 8): "坤为地"
}

def get_mod_result(val, modulus):
    """
    计算取余结果。
    注意：在易学数理中，除尽（余0）通常代表最大值（如8或6）。
    """
    res = val % modulus
    return modulus if res == 0 else res

def split_49():
    """
    模拟将49根蓍草随机分为左右两堆。
    返回 (左边数量, 右边数量)
    """
    # 随机切分，保证每边至少有1根
    left = random.randint(1, 48)
    right = 49 - left
    return left, right

def simulate_concentration_and_wait():
    """
    起卦前的凝神过程
    """
    print("\n" + " " * 4 + "*" * 50)
    print("    【 高岛易断起卦 】")
    print(" " * 4 + "*" * 50)
    print("\n    请调整坐姿，闭目调息，心中默念所测之事...")
    print("\n    >>> 屏息凝神，停止呼吸后将问题聚焦于额头三眼轮处")
    print("    >>> 当间不容发（必须要呼吸时）之际\n")
    
    input("    (气机发动时，请按回车键 Enter 产生卦象)")
    print("")

def simulate_calculation_process(step_name):
    """
    模拟演算过程的动画
    """
    print(f"    正在诚心演算{step_name}...", end="", flush=True)
    # 模拟蓍草分策的耗时
    for _ in range(6):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(" 完成。")
    time.sleep(0.3)

def perform_divination(gender_input):
    # 简单的性别标准化
    g_str = str(gender_input).strip()
    if g_str in ['男', 'Male', 'man', 'm', 'M']:
        gender = '男'
        is_male = True
    else:
        gender = '女'
        is_male = False

    print(f"\n=== 高岛易断模拟程序启动 ===")
    print(f"卜卦人性别: {gender}")
    print(f"总策数: 50 (取1不用，实际演算49)")
    
    # 加入仪式感等待
    simulate_concentration_and_wait()

    print("-" * 40)

    # ==============================
    # 第一次取数 (上卦)
    # 规则: 49分左右。男取左，女取右。除8取余。
    # ==============================
    simulate_calculation_process("上卦")
    
    left, right = split_49()
    
    if is_male:
        taken = left
        side_desc = "左"
    else:
        taken = right
        side_desc = "右"
        
    upper_num = get_mod_result(taken, 8)
    upper_trigram = TRIGRAMS[upper_num]
    
    print(f"[第一次取数] 求上卦")
    print(f"  分策结果: 左{left} / 右{right}")
    print(f"  {gender}性取{side_desc}边: {taken}")
    print(f"  计算: {taken} % 8 = {upper_num} --> 上卦为【{upper_trigram['nature']}{upper_trigram['name']}】")
    print("-" * 40)

    # ==============================
    # 第二次取数 (下卦)
    # 规则: 49分左右。男取右，女取左。除8取余。
    # ==============================
    simulate_calculation_process("下卦")
    
    left, right = split_49()
    
    if is_male:
        taken = right
        side_desc = "右"
    else:
        taken = left
        side_desc = "左"
        
    lower_num = get_mod_result(taken, 8)
    lower_trigram = TRIGRAMS[lower_num]
    
    print(f"[第二次取数] 求下卦")
    print(f"  分策结果: 左{left} / 右{right}")
    print(f"  {gender}性取{side_desc}边: {taken}")
    print(f"  计算: {taken} % 8 = {lower_num} --> 下卦为【{lower_trigram['nature']}{lower_trigram['name']}】")
    print("-" * 40)

    # ==============================
    # 第三次取数 (动爻)
    # 规则: 49分左右。男取左，女取右。除6取余。
    # ==============================
    simulate_calculation_process("动爻")
    
    left, right = split_49()
    
    if is_male:
        taken = left
        side_desc = "左"
    else:
        taken = right
        side_desc = "右"
        
    moving_line = get_mod_result(taken, 6)
    
    print(f"[第三次取数] 求动爻")
    print(f"  分策结果: 左{left} / 右{right}")
    print(f"  {gender}性取{side_desc}边: {taken}")
    print(f"  计算: {taken} % 6 = {moving_line} --> 动爻为【{moving_line}爻】")
    print("=" * 40)

    # ==============================
    # 变卦计算逻辑
    # ==============================
    # 1. 获取本卦的六爻列表 (从下到上)
    # 下卦在下(0,1,2)，上卦在上(3,4,5)
    lower_lines = list(TRIGRAM_LINES[lower_num])
    upper_lines = list(TRIGRAM_LINES[upper_num])
    original_hex_lines = lower_lines + upper_lines
    
    # 2. 变动爻位 (moving_line 是 1-6，对应索引 0-5)
    line_index = moving_line - 1
    # 阴阳互变 (0->1, 1->0)
    original_hex_lines[line_index] = 1 - original_hex_lines[line_index]
    
    # 3. 拆分回上下卦
    new_lower_lines = tuple(original_hex_lines[0:3])
    new_upper_lines = tuple(original_hex_lines[3:6])
    
    # 4. 查找新卦数字
    new_lower_num = LINES_TO_TRIGRAM[new_lower_lines]
    new_upper_num = LINES_TO_TRIGRAM[new_upper_lines]
    
    new_lower_trigram = TRIGRAMS[new_lower_num]
    new_upper_trigram = TRIGRAMS[new_upper_num]
    
    new_hex_name = HEXAGRAM_NAMES.get((new_upper_num, new_lower_num), "未知卦")

    # ==============================
    # 尝试加载外部易经数据
    # ==============================
    try:
        from iching_data import ICHING_DATA
    except ImportError:
        ICHING_DATA = {}

    # ==============================
    # 最终结果输出
    # ==============================
    hex_name = HEXAGRAM_NAMES.get((upper_num, lower_num), "未知卦")
    
    # 获取本卦详情
    orig_data = ICHING_DATA.get((upper_num, lower_num), {})
    orig_judge = orig_data.get("judgement", "（暂无详细卦辞）")
    orig_img = orig_data.get("image", "（暂无大象辞）")
    
    # 获取动爻详情
    line_text = "（暂无该爻辞）"
    takashima_line_text = None
    
    if orig_data and "lines" in orig_data:
        line_text = orig_data["lines"].get(moving_line, "（未录入该爻辞）")
        
    # 获取高岛易断详情
    takashima_general = orig_data.get("takashima", {}).get("general", None)
    if orig_data.get("takashima", {}).get("lines"):
        takashima_line_text = orig_data["takashima"]["lines"].get(moving_line, None)

    # 获取变卦详情
    new_data = ICHING_DATA.get((new_upper_num, new_lower_num), {})
    new_judge = new_data.get("judgement", "（暂无详细卦辞）")
    new_takashima_general = new_data.get("takashima", {}).get("general", None)

    def print_aligned(label, text):
        if not text:
            return
        lines = text.strip().split('\n')
        # 第一行
        print(f"   - {label}: {lines[0]}")
        # 后续行缩进 (对齐到冒号后大致位置)
        # "   - " (5) + 4 chars (8) + ": " (2) = 15 approx
        padding = " " * 15
        for line in lines[1:]:
            if line.strip():
                print(f"{padding}{line.strip()}")

    print(f"\n🔮 最终卦象解读")
    print("=" * 40)
    print(f"1. 本卦 (起初的卦象): 【{hex_name}】")
    print(f"   - 结构: 上{upper_trigram['nature']} 下{lower_trigram['nature']}")
    print(f"   - 卦辞: {orig_judge}")
    print(f"   - 象曰: {orig_img}")
    if takashima_general:
        print_aligned("高岛总断", takashima_general)
    else:
        print(f"   - 象征: 当前的状态或起点")
    
    print(f"\n2. 动爻 (变化的因素): {moving_line}爻动")
    print(f"   - 爻辞: {line_text}")
    
    if takashima_line_text:
        if "【占】" in takashima_line_text:
            # 只保留【占】及之后的内容
            filtered_text = "【占】" + takashima_line_text.split("【占】", 1)[1]
            print_aligned("高岛爻断", filtered_text)
    
    print(f"\n3. 变卦 (事情发展的趋势或结果): 【{new_hex_name}】")
    print(f"   - 结构: 上{new_upper_trigram['nature']} 下{new_lower_trigram['nature']}")
    print(f"   - 卦辞: {new_judge}")
    if new_takashima_general:
        print_aligned("高岛总断", new_takashima_general)
    print(f"   - 象征: 经过变动后，未来的走向或最终结局")
    print("=" * 40)
    print("\n程序结束。")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_gender = sys.argv[1]
    else:
        user_gender = input("请输入卜卦人性别 (男/女): ")
    
    perform_divination(user_gender)
