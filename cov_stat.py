# cov_stat_bar

import matplotlib.pyplot as plt

plt.style.use('ggplot')

m1 = ['March']

m2 = ['April']

m3 = ['May']

m4 = ['June']

m5 = ['July']

m6 = ['Nov']

m7 = ['Dec']

m8 = ['Jan 21']

s1 = [25150]

s2 = [171253]

s3 = [274762]

s4 = [312654]

s5 = [313483]

s6 = [1629656]

s7 = [2488780]

s8 = [3772813]

sm = s1+s2+s3+s4+s5+s6+s7+s8

p = [0,1,2,3,4,5,6,7]

barWidth = 0.4

labels = [*s1,*s2,*s3,*s4,*s5,*s6,*s7,*s8]

plt.bar(m1,s1,width = barWidth,color='#0c7829')

plt.bar(m2,s2,width = barWidth,color='#FA9632')

plt.bar(m3,s3,width = barWidth,color='#a31c17')

plt.bar(m4,s4,width = barWidth,color='#5c5ea1')

plt.bar(m5,s5,width = barWidth,color='#48dbc8')

plt.bar(m6,s6,width = barWidth,color='#569765')

plt.bar(m7,s7,width = barWidth,color='#D9CA71')

plt.bar(m8,s8,width = barWidth,color='#B6DCE0')

for i in range(len(p)):

	plt.text(x=p[i] ,y=sm[i] ,s=labels[i])

plt.title('UK Cases')

plt.xlabel('Months')


plt.show()
