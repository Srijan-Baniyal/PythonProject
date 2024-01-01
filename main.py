import numpy as np
import pandas as pd
import random as rn
import sys
import matplotlib.pyplot as plt


df = pd.read_csv("WCDSV.csv")
pd.set_option("display.max_columns", None)


def menu():
    ans = True
    print("-----Welcome to World Game Analysis System-----")
    print(" 1.Data Visualization \n 2.Data Analysis \n 3.Data Manipulation \n 4.Exit")
    inp = int(input("Enter you choice: "))
    if inp == 1:
        dvisual()
    elif inp == 2:
        danalysis()
    elif inp == 3:
        dmanup()
    elif inp == 4:
        ex = str(input("Are you sure you want to exit ? {y/n}"))
        if ex == "y" or ex == "Y":
            print("Exiting now >>>>> Done !!!")
            sys.exit()
        else:
            print("Invalid Input Try Again")


def dvisual():
    ans = True
    while ans:
        print("----Data Visualization of top 10 Countries---- \n 1.Line Chart-> Countries vs Total Medals \n 2.Bar Chart-> Countries vs Total Number of Gold Medals \n 3.Bar Chart-> Countries vs Total number of Silver Medal \n 4.Bar Chart-> Countries Total number of Bronze Medal \n 5.Histogram-> Countries getting Gold,Silver and Bronze in a given range \n 6.Exit to Main Menu")
        ans = int(input("please enter your choice :  "))
        if ans == 1:
            lchart1()
        elif ans == 2:
            bchart1()
        elif ans == 3:
            bchart2()
        elif ans == 4:
            bchart3()
        elif ans == 5:
            dhistogram()
        elif ans == 6:
            menu()
        else:
            print("Invalid Choice. Try Again")
            continue


def lchart1():
    df = pd.read_csv("WCDSV.csv")
    df.sort_values(by="TotalMedals", ascending=False, inplace=True)
    df = df.loc[:, ["Team", "TotalMedals"]]
    df1 = df.head(10)
    Countries = df1["Team"]
    TotalMedals = df1["TotalMedals"]
    plt.plot(Countries, TotalMedals, linestyle=":", color="green", marker=".")
    x = np.arange(len(Countries))
    plt.xticks(x, Countries, rotation=30)
    plt.xlabel("Country", fontsize=12, color="red")
    plt.ylabel("Total Medals", fontsize=12, color="red")
    plt.title("Total Medals won by top 10 Countries",
              color="blue", fontsize=18)
    plt.show()


def bchart1():
    df = pd.read_csv("WCDSV.csv")
    df.sort_values("Gold", ascending=False)
    df1 = df.head(n=10)
    x = np.arange(len(df1))
    Countries = df1["Team"]
    totalGold = df1["Gold"]
    plt.bar(x+0.25, totalGold, width=.6,
            label="Total number of gold Medals by top 10 countries", color="gold")
    plt.xticks(x, Countries, rotation=30)
    plt.title("World Gold Medal Analysis of top 10 Countries",
              color="blue", fontsize=12)
    plt.xlabel("Countries", fontsize=12, color="red")
    plt.ylabel("Number of Gold Medals", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def bchart2():
    df = pd.read_csv("WCDSV.csv")
    df = df.sort_values("Silver", ascending=False)
    df1 = df.head(n=10)
    x = np.arange(len(df1))
    Countries = df1["Team"]
    TotalSilver = df1["Silver"]
    plt.bar(x+0.25, TotalSilver, width=0.6,
            label="Total Number of Silver Medals by top 10 Countries", color="silver")
    plt.xticks(x, Countries, rotation=30)
    plt.title("World Silver Medal ANalysis of Top 10 Countries",
              color="blue", fontsize=16)
    plt.xlabel("Countries")
    plt.ylabel("Number of Silver Medal", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def bchart3():
    df = pd.read_csv("WCDSV.csv")
    df = df.sort_values("Bronze", ascending=False)
    df1 = df.head(n=10)
    x = np.arange(len(df1))+0.25
    Countries = df1["Team"]
    totalBronze = df["Bronze"]
    plt.bar(x, totalBronze, width=0.6,
            label="Total Number of Bronze Medals By top 10 Countries", color="peru")
    plt.xticks(x, Countries, rotation=30)
    plt.title("World Bronze Medal Analysis of top 10 Countries",
              color="blue", fontsize=16)
    plt.xlabel("Countries", fontsize=12, color="red")
    plt.ylabel("Number of Bronze Medals", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def dhistogram():
    df = pd.read_csv("WCDSV.csv")
    s = df["Silver"]
    g = df["Gold"]
    b = df["Bronze"]
    clm = ["Bronze", "Silver", "Gold"]
    plt.hist([b, s, g], rwidth=0.9, color=[
             "brown", "silver", "gold"], label=clm)
    plt.title("World Game Medal Analysis")
    plt.xlabel("Number of Medals", fontsize=12, color="red")
    plt.ylabel("Number of Countries", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def danalysis():
    while True:
        print("-----DataFrame Analysis-----")
        print(" 1.Print Records of Top Countries In Terms Of Total Medal Won  \n 2.Print Records Of Top Countries In Terms Of Total Gold Medal Won \n 3.Print Records of Top Countries In Terms of Total Silver Medal Won \n 4.Print Records of Top Countries In Terms of Total Bronze Medal Won \n 5.Print Records of Bottom Most Countries In Terms of Medal Won \n 6.Print The General Information About The DataFrame used for Analysis \n 7.Describe The Structure Of The DataFrame used for analysis \n 8.Print The Data of Column Specified By User. \n 9.Print Maximum Value for Each Column In The DataFrame. \n 10.Display Gold,Silver,and Bronze medals won by a Specific Country \n 11.Back To The Main Menu")
        x = int(input("Enter you Choice: "))
        print(f"{x}. Giving Command to the Function ")
        df = pd.read_csv("WCDSV.csv")
        if x == 1:
            df = df.loc[:, ["Team", "TotalMedals"]]
            nor = int(input("Enter the number of Records to be Displayed: "))
            print(f"Top {nor} records of the DataFrame")
            print("----####----")
            print(df.head(nor))
            print("----####----")
        elif x == 2:
            df = df.sort_values("Gold", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Gold"]]
            nor = int(input("Enter the number of Records to be displayed : "))
            print(f"Top {nor} records by total number of gold Medals")
            print("----####----")
            print(df.head(nor))
            print("----####----")
        elif x == 3:
            df = df.sort_values("Silver", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Silver"]]
            nor = int(input("Enter the number of Records to be displayed : "))
            print(f"Top {nor} record by total number of silver medals")
            print("----####----")
            print(df.head(nor))
            print("----####----")
        elif x == 4:
            df = df.sort_values("Bronze", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Bronze"]]
            nor = int(input("Enter the number of records to be displayed : "))
            print(f"Top {nor} records by total number of bronze medal")
            print("----####----")
            print(df.head(nor))
            print("----####----")
        elif x == 5:
            df = df.sort_values(
                "TotalMedals", ascending=False, ignore_index=True)
            nor = int(input("Enter the number of records to be displayed"))
            df = df.loc[:, ["Team", "TotalMedals"]]
            print(f"Bottom {nor} records from the database")
            print("----####----")
            print(df.tail(nor))
            print("----####----")
        elif x == 6:
            print("Information of the Database")
            print("----####----")
            print(df.info())
            print("----####----")
        elif x == 7:
            print("Describing the basic characteristics of the dataframe ")
            print("----####----")
            print(df.describe())
            print("----####----")
        elif x == 8:
            print(f"Name of the column -> {df.columns()}")
            clm = eval(input("Enter the column name in the list"))
            print("----####----")
            print(df[clm])
            print("----####----")
        elif x == 9:
            print(f"Maximum value for each column")
            print("----####----")
            print(df.max())
            print("----####----")
        elif x == 10:
            print("NAme of all participating in  world Games")
            print("----####----")
            print(df["Team"].values)
            print("----####----")
            cntry = eval(input(
                "Enter name of a Country / Countries in the form of like this -['India']:"))
            for cnt in cntry:
                print(df.loc[df["Team"] == cnt, [
                      "Team", "Gold", "Silver", "Bronze"]])
                print("----####----")
        elif x == 11:
            menu()
            break


def dmanup():
    df = pd.read_csv("WCDSV.csv")
    ans = True
    while ans:
        print("----Data Manipulation----")
        print(" 1.Inserting a Row \n 2.Deleting a Row \n 3.Inserting a column \n 4.Deleting a column \n 5.Renaming a column \n 6.Exit to Main Menu")
        ans = int(input("Enter Your Choice: "))
        pd.set_option("display.max_columns", None)
        if ans == 1:
            print("Enter the input in the Following Format")
            col = df.columns
            print(col)
            lst = eval(input("Enter the row values in list: "))
            sr = pd.Series(lst, index=col)
            row_df1 = pd.DataFrame([sr])
            df = pd.concat([row_df1, df], ignore_index=True)
            print(df)
            print("Row Added Successfully")
            print("----####----")
        elif ans == 2:
            inp = int(input("Enter the row's index you want to delete: "))
            df1 = df.drop(inp, axis=0)
            print("----####----")
            print(f"DataFrame after row index number {inp} is deleted")
            print("----####----")
            print(df1)
            print("----####----")
        elif ans == 3:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            clname = str(input("Enter the Column Name"))
            inp = int(
                input("Enter the Column index \n where you want to insert the column: "))
            df.insert(inp, clname, "Nan")
            print(df)
            print("----####----")
        elif ans == 4:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            print("DataFrame before deleting the column")
            print(df)
            inp = input("Enter the column name you want to delete: ")
            df = df.drop(inp, axis=1)
            print(f"DataFrame after deleting the column {inp} : ")
            print(df)
            print("----####----")
        elif ans == 5:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            print("----####----")
            print("DataFrame before changing the column name's")
            print("----####----")
            print(df)
            print("----####----")
        elif ans == 6:
            print("Sending command to the command center >>>>> Done !!!")
            menu()


menu()
