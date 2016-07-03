from joblib import Parallel, delayed
import multiprocessing


# what are your inputs, and what operation do you want to
# perform on each input. For example...



def processInput(i):
    print(i)
    return i * i


if __name__ == "__main__":
    inputs = range(10)
    num_cores = multiprocessing.cpu_count()
    print(num_cores)

    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)

    print(results)
