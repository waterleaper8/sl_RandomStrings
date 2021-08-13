import streamlit as st
import random,string

result = ''

def randomstr(n):
    # 4
    if (ascii_l and not ascii_u and not digit and not symbol):
        randlst = [random.choice(string.ascii_lowercase) for i in range(n)]
    elif (not ascii_l and ascii_u and not digit and not symbol):
        randlst = [random.choice(string.ascii_uppercase) for i in range(n)]
    elif (not ascii_l and not ascii_u and digit and not symbol):
        randlst = [random.choice(string.digits) for i in range(n)]
    elif (not ascii_l and not ascii_u and not digit and symbol):
        randlst = [random.choice(string.punctuation) for i in range(n)]

    # 6
    elif (ascii_l and ascii_u and not digit and not symbol):
        randlst = [random.choice(string.ascii_letters) for i in range(n)]
    elif (ascii_l and not ascii_u and digit and not symbol):
        randlst = [random.choice(string.ascii_lowercase + string.digits) for i in range(n)]
    elif (ascii_l and not ascii_u and not digit and symbol):
        randlst = [random.choice(string.ascii_lowercase + string.punctuation) for i in range(n)]
    elif (not ascii_l and ascii_u and digit and not symbol):
        randlst = [random.choice(string.ascii_uppercase + string.digits) for i in range(n)]
    elif (not ascii_l and ascii_u and not digit and symbol):
        randlst = [random.choice(string.ascii_uppercase + string.punctuation) for i in range(n)]
    elif (not ascii_l and not ascii_u and digit and symbol):
        randlst = [random.choice(string.digits + string.punctuation) for i in range(n)]
    
    # 4
    elif (ascii_l and ascii_u and digit and not symbol):
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    elif (ascii_l and ascii_u and not digit and symbol):
        randlst = [random.choice(string.ascii_letters + string.punctuation) for i in range(n)]
    elif (ascii_l and not ascii_u and digit and symbol):
        randlst = [random.choice(string.ascii_lowercase + string.digits + string.punctuation) for i in range(n)]
    elif (not ascii_l and ascii_u and digit and symbol):
        randlst = [random.choice(string.ascii_uppercase + string.digits + string.punctuation) for i in range(n)]

    # 1
    elif (ascii_l and ascii_u and digit and symbol):
        randlst = [random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(n)]
    else:
        return 'どれかチェックを入れてください'
    return ''.join(randlst)

st.set_page_config(page_title='ランダム文字列生成', initial_sidebar_state = 'auto')
st.title('ランダム文字列生成')

st.subheader('組み合わせを選択してください')
ascii_l = st.checkbox('英小文字')
ascii_u = st.checkbox('英大文字')
digit = st.checkbox('数字')
symbol = st.checkbox('記号')

st.subheader('生成したい文字数を入力してください（32文字まで）')
n = st.number_input('', min_value=1, max_value=32, step=1, value=13)
gen_button = st.button('文字列を生成')

# placeholder = st.empty()
# gen_area = placeholder.text_input('Generated Strings')

if gen_button:
    result = randomstr(n)
    # gen_area = placeholder.text_input('Generated Strings', value=result)
    st.code(result)

# copy_button = st.button('文字列をコピー')