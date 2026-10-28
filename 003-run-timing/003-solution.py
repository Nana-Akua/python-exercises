
#function that ask for running time
def run_timing():

    total_time = 0
    num_of_runs = 0

    while True:
        one_run = input("Enter 10 km run time: ")

        #used to evaluate whether a response is empty or not
        if not one_run:
            break

        total_time += float(one_run)
        num_of_runs += 1

    avg_time = total_time/num_of_runs
    print(f"Average of {avg_time: .2f}, over {num_of_runs} runs")\

run_timing()