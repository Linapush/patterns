# from random import randint, choice

# names = ['Maxim', 'Kirill']

# persons = [(choice(names), randint(1, 65)) for _ in range(15)]
# persons = [(num, person) for num, person in enumerate(persons)]

# for record in (sorted(persons, key=lambda x: (x[1][0], x[1][1]))):
#     print(record)

# from random import randint, choice

# manfs_cpu = ['AMD', 'Intel']
# manfs_gpu = ['Nvidia', 'AMD', 'Intel']

# #CREATE INDEX ON pcs using binary_tree(cpu, gpu, price)
# pcs = [(id_, choice(manfs_cpu), choice(manfs_gpu), randint(10, 100)) for id_ in range(15)]
# for record in sorted(pcs, key=lambda x: (x[1], x[2], x[3])):
#     print(record)

from random import randint, choice

manfs_cpu = ['AMD', 'Intel']
manfs_gpu = ['Nvidia', 'AMD', 'Intel']

#CREATE INDEX ON pcs using binary_tree(cpu, gpu, price)
pcs = [(id_, choice(manfs_cpu), choice(manfs_gpu), randint(10, 100)) for id_ in range(15)]
for record in sorted(pcs, key=lambda x: (x[2], x[1], x[3])):
    print(record)


