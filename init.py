def compare_lists(name_a, a, name_b, b):
    # exist_list = [item for item in a if item in b]
    exist_list = set(a) & set(b)
    print("{} compare {}".format(name_a, name_b))
    print(exist_list)

apr_2_2023 = [6316, 1177, 5237, 2109, 970, 3196, 9752, 4495, 2174, 6107, 8926, 9094,
              1733, 742, 544, 9885, 8040, 2219, 9824, 4829, 216, 486, 6256]

mar_29_2023 = [890, 7046, 9310, 2940, 5796, 5268, 9781, 1978, 3322, 108, 2511, 3225,
               7697, 5810, 6471, 7352, 9708, 324, 4468, 3439, 7721, 5083, 2917]

mar_26_2023 = [23, 1446, 8258, 8551, 9534, 3626, 4230, 2795, 642, 1537, 4296, 6050,
               3571, 2522, 607, 5444, 1255, 3290, 6493, 7720, 5884, 9677, 4973, 6316]

full_list = [("2/4/2023", apr_2_2023), ("26/3/2023", mar_26_2023), ("29/3/2023", mar_29_2023)]

for i in range(len(full_list)):
    for j in range(i + 1, len(full_list)):
        compare_lists(full_list[i][0], full_list[i][1], full_list[j][0], full_list[j][1])
