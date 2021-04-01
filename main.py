import streamlit as st
import random,string

def randomstr(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

st.title('ランダム文字列生成')
st.subheader('生成したい文字数を入力してください（32文字まで）')
n = st.number_input('', min_value=0, max_value=32, step=1)

gen_button = st.button('文字列を生成')
if gen_button:
    st.write(f'{randomstr(n)}')