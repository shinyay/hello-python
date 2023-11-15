from tqdm import tqdm
import time

def main():
    for i in tqdm(range(100)):
        time.sleep(1)

# def main():
#     print("Hello Python")

# if __name__  == "__main__":
#     main()