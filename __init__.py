import os


def threshold(parent_directory):
    thresholds = []
    x = [x[0] for x in os.walk(parent_directory)]
    times = len(x) - 1
    for n in range(0, times):
        similarity = calulate_threshold(x[n+1])
        thresholds.append(similarity)
    return thresholds


def calulate_threshold(child_directory):
    mean = 0
    class_sum = 0
    n = 0
    index = 0
    mean_list = []

    for path, _, files in os.walk(child_directory):
        for file_name in files:
            filepath = os.path.join(path, file_name)

            print(f"Checking --> {filepath}")

            filename_1 = filepath

            for path, _, files in os.walk(child_directory):
                for file_name in files:
                    filepath = os.path.join(path, file_name)

                    filename_2 = filepath

                    # Program to measure the similarity between
                    # two sentences using cosine similarity.

                    A = open(filename_1, encoding='utf-8')
                    B = open(filename_2, encoding='utf-8')

                    X = A.read()
                    Y = B.read()

                    # tokenization
                    X_list = X.split()
                    Y_list = Y.split()

                    l1 = []
                    l2 = []

                    X_set = {w for w in X_list}
                    Y_set = {w for w in Y_list}

                    # form a set containing keywords of both strings
                    rvector = X_set.union(Y_set)
                    for w in rvector:
                        if w in X_set:
                            l1.append(1)  # create a vector
                        else:
                            l1.append(0)
                        if w in Y_set:
                            l2.append(1)
                        else:
                            l2.append(0)
                    c = 0

                    # cosine formula
                    for i in range(len(rvector)):
                        c += l1[i]*l2[i]
                    cosine = c / float((sum(l1)*sum(l2))**0.5)
                    n += 1
                    if cosine != 0:
                        class_sum += cosine

            mean = class_sum/n
            mean_list.insert(index, mean)
            index += 1
    threshold = min(mean_list)

    return threshold


def similarity(file, parent_directory, thresholds):
    topic = False
    similarity_score = []
    x = [x[0] for x in os.walk(parent_directory)]
    times = len(x) - 1
    for n in range(0, times):
        similarity = calcualte_similarity(file, x[n+1])
        similarity_score.append(similarity)

    sim_length = len(similarity_score)
    for n in range(0, sim_length):
        if similarity_score[n] >= thresholds[n]:
            topic = True
    return topic


def calcualte_similarity(file, child_directory):
    class_mean = 0
    class_sum = 0
    n = 0

    for path, _, files in os.walk(child_directory):
        for file_name in files:
            filepath = os.path.join(path, file_name)

            filename_1 = filepath

            # Program to measure the similarity between
            # two sentences using cosine similarity.

            filename_2 = file
            A = open(filename_1, encoding='utf-8')
            B = open(filename_2, encoding='utf-8')

            X = A.read()
            Y = B.read()

            # tokenization
            X_list = X.split()
            Y_list = Y.split()

            l1 = []
            l2 = []

            X_set = {w for w in X_list}
            Y_set = {w for w in Y_list}

            # form a set containing keywords of both strings
            rvector = X_set.union(Y_set)
            for w in rvector:
                if w in X_set:
                    l1.append(1)  # create a vector
                else:
                    l1.append(0)
                if w in Y_set:
                    l2.append(1)
                else:
                    l2.append(0)
            c = 0

            # cosine formula
            for i in range(len(rvector)):
                c += l1[i]*l2[i]
            cosine = c / float((sum(l1)*sum(l2))**0.5)
            n += 1
            if cosine != 0:
                class_sum += cosine
    class_mean = class_sum/n
    return class_mean
