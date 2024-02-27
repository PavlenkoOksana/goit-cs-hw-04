import multiprocessing
import time

def search_keywords(file, keyword, result_queue):
    try:
        with open(file, 'r') as f:
            content = f.read()
            if keyword in content:
                result_queue.put(file)
    except Exception as e:
        print(f"Error processing file {file}: {e}")

def process_files(files, keyword, result_queue):
    for file in files:
        search_keywords(file, keyword, result_queue)

def split_files_and_process(num_processes, all_files, keyword):
    result_queue = multiprocessing.Queue()
    files_per_process = len(all_files) // num_processes
    processes = []

    start_time = time.time()

    for i in range(0, len(all_files), files_per_process):
        process_files_list = all_files[i:i + files_per_process]
        process = multiprocessing.Process(target=process_files, args=(process_files_list, keyword, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Multiprocessing Execution Time: {execution_time:.4f} seconds")

    result_list = []
    while not result_queue.empty():
        result_list.append(result_queue.get())

    result_dict_multiprocessing = {keyword: result_list}
    return result_dict_multiprocessing

if __name__ == "__main__":
    all_files = ["D:/Projects/My_Repository/goit-cs-hw-04/goit-cs-hw-04/file1.txt", "D:\Projects\My_Repository\goit-cs-hw-04\goit-cs-hw-04/file2.txt", "D:\Projects\My_Repository\goit-cs-hw-04\goit-cs-hw-04/file3.txt", "D:\Projects\My_Repository\goit-cs-hw-04\goit-cs-hw-04/file4.txt"]
    keyword_to_search = "keyword"
    num_processes = 2

    result_dict_multiprocessing = split_files_and_process(num_processes, all_files, keyword_to_search)
    print(result_dict_multiprocessing)