import os
from subprocess import Popen, PIPE, call


class Plots:
    def __init__(self, graphType):
        #graphType is volcano
        self.graphType = graphType
     
        self.my_env = os.environ.copy()
        self.script_path = os.getcwd()        

    def plot(self):
        try:
            os.mkdir(str(self.graphType)+"Output")
           
        except FileExistsError:
            pass

        self.__volcano__()

    def __volcano__(self):
        
        analyses_dir = os.getcwd()
      
        #input directory for volcano plots is W:\FastQ\wpoon\graphs
        #input directory contains a separate directory for each type 
        graphs_dir = analyses_dir + "\\" + "graphs"
        print(graphs_dir)

        #directory refers to gene (ex: AST. iMGL, etc.)
        for directory in os.listdir(graphs_dir):
            if directory.split(".")[-1] != "zip" and directory.split(".")[-1] != "DS_Store" :
                for filename in os.listdir( graphs_dir + '\\' + directory):
                    if "differentialexpression" in filename.lower():
                     
                        print(filename)
                        args = ["Rscript", analyses_dir + "\\" + "volcano.R",
                            graphs_dir + "\\" + directory + "\\" + filename,
                            self.script_path + "\\" + self.graphType+"Output", 
                            filename, directory]
                        print(args)
                        process = Popen(args, stdout = PIPE, stderr = PIPE)
                        out, error = process.communicate()
                        exitcode = process.returncode
                        print(exitcode)
                        print(out)
                        print(error)

            
            
if __name__ == "__main__":
    #change list to just abbreviation
    graphs = Plots("volcano")
    graphs.plot()

