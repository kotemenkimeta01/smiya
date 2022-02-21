import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
# from sympy import continued_fraction_periodic
import time

st.title('Streamlit 超入門2')

st.write('プログレスバー')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ１')
expander.write(('問い合わせ１の回答'))
expander = st.expander('問い合わせ２')
expander.write(('問い合わせ２の回答'))
expander = st.expander('問い合わせ３')
expander.write(('問い合わせ３の回答'))

# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？',0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition

# st.sidebar.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は？',0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition


# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='sight', use_column_width=True)


# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )


# st.map(df)



# st.table(df.style.highlight_max(axis=0) )

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

