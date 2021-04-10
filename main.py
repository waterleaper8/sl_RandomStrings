import streamlit as st
import random,string
# import pyperclip

result = ''

def randomstr(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

st.title('ランダム文字列生成')
st.subheader('生成したい文字数を入力してください（32文字まで）')

# numselect = range(8, 32)
# st.selectbox('Select', numselect)

n = st.number_input('', min_value=1, max_value=32, step=1)
gen_button = st.button('文字列を生成')

placeholder = st.empty()
gen_area = placeholder.text_input('Generated Strings')

# copy_button = st.button('コピー')

if gen_button:
    result = randomstr(n)
    gen_area = placeholder.text_input('Generated Strings', value=result)

# if copy_button:
#     # result2 = gen_area.get_option(value)
#     pyperclip.copy(resul2)
