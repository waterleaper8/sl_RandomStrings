import streamlit as st
import random,string

result = ''

def randomstr(n):
    chars = ''
    if (ascii_l):
        chars += string.ascii_lowercase
    if (ascii_u):
        chars += string.ascii_uppercase
    if (digit):
        chars += string.digits
    if (symbol):
        chars += string.punctuation
    if (chars == ''):
        return 'どれかチェックを入れてください'
    else:
        randlst = [random.choice(chars) for i in range(n)]
    return ''.join(randlst)

st.set_page_config(page_title='パスワード生成アプリ', initial_sidebar_state = 'auto')
st.title('パスワード生成アプリ')

st.subheader('組み合わせを選択してください')
ascii_l = st.checkbox('英小文字', True)
ascii_u = st.checkbox('英大文字', True)
digit = st.checkbox('数字', True)
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
