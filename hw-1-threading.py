import threading
import time

def search_keywords(file, keyword, result_dict):
    try:
        with open(file, 'r') as f:
            content = f.read()
            if keyword in content:
                result_dict[keyword].append(file)
    except Exception as e:
        print(f"Error processing file {file}: {e}")

def process_files(files, keyword, result_dict):
    for file in files:
        search_keywords(file, keyword, result_dict)

def split_files_and_process(num_threads, all_files, keyword):
    result_dict = {keyword: []}
    files_per_thread = len(all_files) // num_threads
    threads = []

    start_time = time.time()

    for i in range(0, len(all_files), files_per_thread):
        thread_files = all_files[i:i + files_per_thread]
        thread = threading.Thread(target=process_files, args=(thread_files, keyword, result_dict))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Threading Execution Time: {execution_time:.4f} seconds")
    return result_dict

if __name__ == "__main__":
    all_files = ["D:/Projects/My_Repository/goit-cs-hw-04/goit-cs-hw-04/file1.txt", "D:\Projects\My_Repository\goit-cs-hw-04\goit-cs-hw-04/file2.txt", "D:\Projects\My_Repository\goit-cs-hw-04\goit-cs-hw-04/file3.txt", "D:\Projects\My_Repository\goit-cs-hw-04\goit-cs-hw-04/file4.txt"]
    keyword_to_search = "keyword"
    num_threads = 2

    result_dict_threading = split_files_and_process(num_threads, all_files, keyword_to_search)
    print(result_dict_threading)