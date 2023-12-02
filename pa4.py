#Jackson Sanders
#028675372
import sys
import csv

def main():
    
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file)
        num_dict = {}
       
        for line in csv_reader:
            num = int(line[0])
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        num_freq_pairs = [(k, v) for k, v in num_dict.items() if v > 1]
        sorted_pairs = sorted(num_freq_pairs, key=lambda x: x[1], reverse=True)
        
        with open(sys.argv[2], mode='w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            
            for pair in sorted_pairs:
                csv_writer.writerow([pair[0], pair[1]])
main()

            