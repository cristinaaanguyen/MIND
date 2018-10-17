import os
from subprocess import Popen, PIPE, call


class Plots:
    def __init__(self, graphType):
        #graphType is corrplot
        #take in a file path instead, if the file ends with .csv, split it at the period and use the name in the output
        self.graphType = graphType
     
        self.my_env = os.environ.copy()
        self.script_path = os.getcwd()
        self.corrplots_input_files_directory = self.script_path + "\\CorrplotsInput"
        

    def plot(self):
        try:
            os.mkdir(str(self.graphType)+"Output")
           
        except FileExistsError:
            pass

        for filename in os.listdir(self.corrplots_input_files_directory):
            #filename is file name in the corrplots input
            #uncomment the line if you only want to run one of the functions 
            self.__corrplot__(filename)
            self.corrplotFull(filename)


    def __corrplot__(self, i):
        print("script path:" + self.script_path)
        #input i will be the input file name in CorrplotsInput directory
        
        parse_file = i.split(".")
        if parse_file[1] == "csv":

            args = ["Rscript", self.script_path + "\\" + "corrplots.R",
                self.script_path + "\\" + 'CorrplotsInput' + "\\" + i,
                self.script_path + "\\" + self.graphType + "Output",
                parse_file[0]]
            #parse_file[0] is arg[3] parameter in R Script when making the images
            process = Popen(args, stdout = PIPE, stderr = PIPE)
            out, error = process.communicate()
            exitcode = process.returncode
            print(exitcode)
            print(out)
            print(error)
        else:
            print(i + " is not a csv file")


    #run this code if you want a full corrplot (not just half), this code calls the corrplotComplete.R script
    def corrplotFull(self, i):
        parse_file = i.split(".")
        if parse_file[1] == "csv":
            args = ["Rscript", self.script_path + "\\" + "corrplotComplete.R",
                self.script_path + "\\" + 'CorrplotsInput' + "\\" + i,
                self.script_path + "\\" + self.graphType + "Output",
                parse_file[0]]
            process = Popen(args, stdout = PIPE, stderr = PIPE)
            out, error = process.communicate()
            exitcode = process.returncode
            print(args)
            print(exitcode)
            print(out)
            print(error)


            
            
if __name__ == "__main__":

     corrplots = Plots("corrplot")
     corrplots.plot()


     
        
