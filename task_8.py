import matplotlib.pyplot as plt

labels = ['2018', '2019', '2020']
values = [30, 45, 37]
plt.figure(figsize=(5,5), dpi=100)

bars = plt.bar(labels, values)
plt.xlabel('Years')
plt.ylabel('Avg order cost')

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.savefig('barchart.png', dpi=300)