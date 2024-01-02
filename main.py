import numpy as np
import pandas as pd
import random as rn
import sys
import matplotlib.pyplot as plt
from rich.console import Console
from colorama import Fore, init
import colorama

console = Console()
colorama.init()

df = pd.read_csv("WCDSV.csv")
pd.set_option("display.max_columns", None)
RED = "\x1b[1;31;40m"



def hook(tp, *args):
    if tp is KeyboardInterrupt:
        print(colorama.Fore.RESET)
        exit()


def colored_input(text: str, color):
    sys.excepthook = hook
    inp = input(text + color)
    print(colorama.Fore.RESET, end="", flush=True)
    sys.excepthook = sys.__excepthook__
    return inp


def menu():
    ans = True
    console.print(
        "----- Welcome to World Game Analysis System -----", style="green4")
    console.print("-----#####-----", style="red1")
    console.print(
        " [green]1.Data Visualization[/] \n [yellow]2.Data Analysis[/] \n [deep_pink4]3.Data Manipulation[/] \n [purple]4.Exit[/]")
    console.print("-----#####-----", style="red1")
    inp = int(colored_input(f"{RED}Enter you choice: ", colorama.Fore.GREEN))
    if inp == 1:
        dvisual()
    elif inp == 2:
        danalysis()
    elif inp == 3:
        dmanup()
    elif inp == 4:
        ex = str(colored_input(
            "Are you sure you want to exit ? {y/n}: ", colorama.Fore.RED))
        if ex == "y" or ex == "Y":
            console.print("Exiting now >>>>> Done !!!", style="green4")
            sys.exit()
        else:
            menu()


def dvisual():
    ans = True
    while ans:
        console.print("-----#####-----", style="red1")
        console.print("[green]-----Data Visualization of top 10 Countries-----[/] \n [dark_goldenrod]1.Line Chart-> Countries vs Total Medals[/] \n [sky_blue1]2.Bar Chart-> Countries vs Total Number of Gold Medals[/] \n [cyan3]3.Bar Chart-> Countries vs Total number of Silver Medal[/] \n [gray63]4.Bar Chart-> Countries Total number of Bronze Medal[/] \n [cyan1]5.Histogram-> Countries getting Gold,Silver and Bronze in a given range[/] \n [purple]6.Exit to Main Menu[/]")
        console.print("-----#####-----", style="red1")
        ans = int(colored_input(
            "please enter your choice :  ", colorama.Fore.GREEN))
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
            console.print("Invalid Choice. Try Again")
            continue


def lchart1():
    df = pd.read_csv("WCDSV.csv")
    df.sort_values(by="TotalMedals", ascending=False, inplace=True)
    df = df.loc[:, ["Team", "TotalMedals"]]
    df1 = df.head(10)
    Countries = df1["Team"]
    TotalMedals = df1["TotalMedals"]
    plt.plot(Countries, TotalMedals, linestyle=":",
             color="green", marker=".", markerfacecolor="black")
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
            label="Total Number of Silver Medals by top 10 Countries", color="lime")
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
        console.print("-----DataFrame Analysis-----", style="green4")
        console.print("-----#####-----", style="red1")
        console.print(" [dark_goldenrod]1.Print Records of Top Countries In Terms Of Total Medal Won[/]  \n [dark_orange3]2.Print Records Of Top Countries In Terms Of Total Gold Medal Won[/] \n [dark_khaki]3.Print Records of Top Countries In Terms of Total Silver Medal Won[/] \n [deep_pink4]4.Print Records of Top Countries In Terms of Total Bronze Medal Won[/] \n [thistle1]5.Print Records of Bottom Most Countries In Terms oF Medal Won[/] \n [sandy_brown]6.Print The General Information About The DataFrame used for Analysis[/] \n [plum1]7.Describe The Structure Of The DataFrame used for analysis[/] \n [indian_red1]8.Print The Data of Column Specified By User[indian_red1]. \n [dark_goldenrod]9.Print Maximum Value for Each Column In The DataFrame.[/] \n [dark_khaki]10.Display Gold,Silver,and Bronze medals won by a Specific Country[/] \n [purple]11.Back To The Main Menu[/]")
        console.print("-----#####-----", style="red1")
        x = int(colored_input("Enter you Choice: ", colorama.Fore.GREEN))
        df = pd.read_csv("WCDSV.csv")
        if x == 1:
            df = df.loc[:, ["Team", "TotalMedals"]]
            nor = int(colored_input(
                "Enter the number of Records to be Displayed: "))
            console.print(
                f"Top {nor} records of the DataFrame", style="salmon1")
            console.print("----####----", style="red1")
            console.print(df.head(nor))
            console.print("----####----", style="red1")
        elif x == 2:
            df = df.sort_values("Gold", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Gold"]]
            nor = int(colored_input(
                "Enter the number of Records to be displayed : "))
            console.print(
                f"Top {nor} records by total number of gold Medals", style="salmon1")
            console.print("-----#####-----", style="red1")
            console.print(df.head(nor))
            console.print("-----#####-----", style="red1")
        elif x == 3:
            df = df.sort_values("Silver", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Silver"]]
            nor = int(colored_input(
                "Enter the number of Records to be displayed : "))
            console.print(
                f"Top {nor} record by total number of silver medals", style="salmon1")
            console.print("-----#####-----", style="red1")
            console.print(df.head(nor))
            console.print("-----#####-----", style="red1")
        elif x == 4:
            df = df.sort_values("Bronze", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Bronze"]]
            nor = int(colored_input(
                "Enter the number of records to be displayed : "))
            console.print(
                f"Top {nor} records by total number of bronze medal", style="salmon1")
            console.print("-----#####-----", style="red1")
            console.print(df.head(nor))
            console.print("-----#####-----", style="red1")
        elif x == 5:
            df = df.sort_values(
                "TotalMedals", ascending=False, ignore_index=True)
            nor = int(colored_input(
                "Enter the number of records to be displayed: "))
            df = df.loc[:, ["Team", "TotalMedals"]]
            console.print(
                f"Bottom {nor} records from the database", style="salmon1")
            console.print("-----#####----", style="red1")
            console.print(df.tail(nor))
            console.print("-----#####----", style="red1")
        elif x == 6:
            console.print("Information of the Database", style="green1")
            console.print("-----#####----", style="red1")
            console.print(df.info())
            console.print("-----#####-----", style="red1")
        elif x == 7:
            console.print(
                "Describing the basic characteristics of the dataframe ", style="green1")
            console.print("-----#####-----", style="red1")
            console.print(df.describe())
            console.print("-----#####-----", style="red1")
        elif x == 8:
            console.print(
                f"Name of the column -> {df.columns}", style="green1")
            clm = str(colored_input("Enter the column name in the list: "))
            console.print("-----#####-----", style="red1")
            console.print(df[clm])
            console.print("-----#####-----", style="red1")
        elif x == 9:
            console.print(f"Maximum value for each column", style="green1")
            console.print("----####----", style="red1")
            console.print(df.max())
            console.print("----####----", style="red1")
        elif x == 10:
            console.print(
                "Name of all participating in  world Games", style="green1")
            console.print("-----#####-----", style="red1")
            console.print(df["Team"].values)
            console.print("-----#####-----", style="red1")
            cntry = eval(colored_input(
                "Enter name of a Country / Countries in the form of like this -['India']:"))
            for cnt in cntry:
                console.print(df.loc[df["Team"] == cnt, [
                    "Team", "Gold", "Silver", "Bronze"]])
                console.print("-----#####-----", style="red1")
        elif x == 11:
            menu()
            break


def dmanup():
    df = pd.read_csv("WCDSV.csv")
    ans = True
    while ans:
        console.print("-----Data Manipulation-----", style="green4")
        console.print("-----#####-----", style="red1")
        console.print(
            " [dark_sea_green]1.Inserting a Row[/] \n [sky_blue2]2.Deleting a Row[/] \n [pale_turquoise1]3.Inserting a column[/] \n [orchid]4.Deleting a column[/] \n [gold3]5.Renaming a column[/] \n [purple]6.Exit to Main Menu[/]")
        console.print("-----#####-----", style="red1")
        ans = int(colored_input("Enter Your Choice: ", colorama.Fore.GREEN))
        pd.set_option("display.max_columns", None)
        if ans == 1:
            console.print("Enter the colored_input in the Following Format")
            col = df.columns
            console.print(col)
            lst = eval(colored_input("Enter the row values in list: "))
            sr = pd.Series(lst, index=col)
            row_df1 = pd.DataFrame([sr])
            df = pd.concat([row_df1, df], ignore_index=True)
            console.print(df)
            console.print("Row Added Successfully")
            console.print("----####----")
        elif ans == 2:
            inp = int(colored_input(
                "Enter the row's index you want to delete: "))
            df1 = df.drop(inp, axis=0)
            console.print("----####----")
            console.print(f"DataFrame after row index number {inp} is deleted")
            console.print("----####----")
            console.print(df1)
            console.print("----####----")
        elif ans == 3:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            clname = str(colored_input("Enter the Column Name : "))
            inp = int(
                colored_input("Enter the Column index \n where you want to insert the column: "))
            df.insert(inp, clname, "Nan")
            console.print(df)
            console.print("----####----")
        elif ans == 4:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            console.print("DataFrame before deleting the column")
            console.print(df)
            inp = colored_input("Enter the column name you want to delete: ")
            df = df.drop(inp, axis=1)
            console.print(f"DataFrame after deleting the column {inp} : ")
            console.print(df)
            console.print("----####----")
        elif ans == 5:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            console.print("----####----")
            console.print("DataFrame before changing the column name's")
            console.print("----####----")
            console.print(df)
            console.print("----####----")
            oldcm = str(
                colored_input("Enter the name of the column you want to change: "))
            newcm = str(colored_input("Enter the new name of the column: "))
            df = df.rename(columns={oldcm: newcm})
            console.print("-----#####-----", style="red1")
            console.print("DataFrame after changing the column name's")
            console.print("-----#####-----", style="red1")
            console.print(df)
            console.print("----#####-----", style="red1")
        elif ans == 6:
            console.print(
                "Sending command to the command center >>>>> Done !!!")
            menu()


menu()
