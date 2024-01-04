import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from rich.console import Console
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
    inp = int(colored_input(f"{RED}Enter you choice: ", colorama.Fore.RED))
    if inp == 1:
        visual()
    elif inp == 2:
        analysis()
    elif inp == 3:
        operations()
    elif inp == 4:
        ex = str(colored_input(
            f"{RED}Are you sure you want to exit ? (y or n): ", colorama.Fore.RED))
        if ex == "y" or ex == "Y":
            console.print("Exiting now >>>>> Done !!!", style="green4")
            sys.exit()
        else:
            menu()


def visual():
    ans = True
    while ans:
        console.print("-----#####-----", style="red1")
        console.print("[green]-----Data Visualization of top 10 Countries-----[/] \n [dark_goldenrod]1.Line Chart-> Countries vs Total Medals[/] \n [sky_blue1]2.Bar Chart-> Countries vs Total Number of Gold Medals[/] \n [cyan3]3.Bar Chart-> Countries vs Total number of Silver Medal[/] \n [gray63]4.Bar Chart-> Countries Total number of Bronze Medal[/] \n [cyan1]5.Histogram-> Countries getting Gold,Silver and Bronze in a given range[/] \n [purple]6.Exit to Main Menu[/]")
        console.print("-----#####-----", style="red1")
        ans = int(colored_input(
            f"{RED}please enter your choice :  ", colorama.Fore.RED))
        if ans == 1:
            chart1()
        elif ans == 2:
            chart2()
        elif ans == 3:
            chart3()
        elif ans == 4:
            chart4()
        elif ans == 5:
            histogram()
        elif ans == 6:
            menu()
        else:
            console.print("Invalid Choice. Try Again")
            continue


def chart1():
    df = pd.read_csv("WCDSV.csv")
    df.sort_values(by="TotalMedals", ascending=True, inplace=True)
    df = df.loc[:, ["Team", "TotalMedals"]]
    df1 = df.tail(10)
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


def chart2():
    df = pd.read_csv("WCDSV.csv")
    df.sort_values("Gold", ascending=True)
    df1 = df.head(10)
    x = np.arange(len(df1))
    Countries = df1["Team"].tolist()
    totalGold = df1["Gold"].tolist()
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


def chart3():
    df = pd.read_csv("WCDSV.csv")
    df = df.sort_values("Silver", ascending=True)
    df1 = df.tail(10)
    x = np.arange(len(df1))
    Countries = df1["Team"].tolist()
    TotalSilver = df1["Silver"].tolist()
    plt.bar(x+0.25, TotalSilver, width=0.6,
            label="Total Number of Silver Medals by top 10 Countries", color="lime")
    plt.xticks(x, Countries, rotation=30)
    plt.title("World Silver Medal Analysis of Top 10 Countries",
              color="blue", fontsize=16)
    plt.xlabel("Countries")
    plt.ylabel("Number of Silver Medal", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def chart4():
    df = pd.read_csv("WCDSV.csv")
    df = df.sort_values("Bronze", ascending=True)
    df1 = df.tail(10)
    x = np.arange(len(df1))
    Countries = df1["Team"].tolist()
    totalBronze = df1["Bronze"].tolist()
    plt.bar(Countries, totalBronze, width=0.6,
            label="Total Number of Bronze Medals By top 10 Countries", color="peru")
    plt.xticks(x + 0.25, Countries, rotation=30)
    plt.title("World Bronze Medal Analysis of top 10 Countries",
              color="blue", fontsize=16)
    plt.xlabel("Countries", fontsize=12, color="red")
    plt.ylabel("Number of Bronze Medals", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def histogram():
    df = pd.read_csv("WCDSV.csv")
    g = df["Gold"]
    s = df["Silver"]
    b = df["Bronze"]
    clm = ["Gold", "Silver", "Bronze"]
    plt.hist([g, s, b], rwidth=0.9, color=[
        "gold", "silver", "brown"], label=clm)
    plt.title("World Game Medal Analysis")
    plt.xlabel("Number of Medals", fontsize=12, color="red")
    plt.ylabel("Number of Countries", fontsize=12, color="red")
    plt.grid()
    plt.legend()
    plt.show()


def analysis():
    while True:
        console.print("-----DataFrame Analysis-----", style="green4")
        console.print("-----#####-----", style="red1")
        console.print(" [dark_goldenrod]1.Print Records of Top Countries In Terms Of Total Medal Won[/]  \n [dark_orange3]2.Print Records Of Top Countries In Terms Of Total Gold Medal Won[/] \n [dark_khaki]3.Print Records of Top Countries In Terms of Total Silver Medal Won[/] \n [deep_pink4]4.Print Records of Top Countries In Terms of Total Bronze Medal Won[/] \n [thistle1]5.Print Records of Bottom Most Countries In Terms oF Medal Won[/] \n [sandy_brown]6.Print The General Information About The DataFrame used for Analysis[/] \n [plum1]7.Describe The Structure Of The DataFrame used for analysis[/] \n [indian_red1]8.Print The Data of Column Specified By User[indian_red1]. \n [dark_goldenrod]9.Print Maximum Value for Each Column In The DataFrame.[/] \n [dark_khaki]10.Display Gold,Silver,and Bronze medals won by a Specific Country[/] \n [purple]11.Back To The Main Menu[/]")
        console.print("-----#####-----", style="red1")
        x = int(colored_input(f"{RED}Enter you Choice: ", colorama.Fore.RED))
        df = pd.read_csv("WCDSV.csv")
        if x == 1:
            df = df.loc[:, ["Team", "TotalMedals"]]
            nor = int(colored_input(
                f"{RED}Enter the number of Records to be Displayed: ", colorama.Fore.RED))
            console.print(
                f"Top {nor} records of the DataFrame", style="salmon1")
            console.print("----####----", style="red1")
            console.print(df.head(nor))
            console.print("----####----", style="red1")
        elif x == 2:
            df = df.sort_values("Gold", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Gold"]]
            nor = int(colored_input(
                f"{RED}Enter the number of Records to be displayed : ", colorama.Fore.RED))
            console.print(
                f"Top {nor} records by total number of gold Medals", style="salmon1")
            console.print("-----#####-----", style="red1")
            console.print(df.head(nor))
            console.print("-----#####-----", style="red1")
        elif x == 3:
            df = df.sort_values("Silver", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Silver"]]
            nor = int(colored_input(
                f"{RED}Enter the number of Records to be displayed : ", colorama.Fore.RED))
            console.print(
                f"Top {nor} record by total number of silver medals", style="salmon1")
            console.print("-----#####-----", style="red1")
            console.print(df.head(nor))
            console.print("-----#####-----", style="red1")
        elif x == 4:
            df = df.sort_values("Bronze", ascending=False, ignore_index=True)
            df = df.loc[:, ["Team", "Bronze"]]
            nor = int(colored_input(
                f"{RED}Enter the number of records to be displayed : ", colorama.Fore.RED))
            console.print(
                f"Top {nor} records by total number of bronze medal", style="salmon1")
            console.print("-----#####-----", style="red1")
            console.print(df.head(nor))
            console.print("-----#####-----", style="red1")
        elif x == 5:
            df = df.sort_values(
                "TotalMedals", ascending=False, ignore_index=True)
            nor = int(colored_input(
                f"{RED}Enter the number of records to be displayed: ", colorama.Fore.RED))
            df = df.loc[:, ["Team", "TotalMedals"]]
            console.print(
                f"Bottom {nor} records from the database", style="salmon1")
            console.print("-----#####----", style="red1")
            console.print(df.tail(nor))
            console.print("-----#####----", style="red1")
        elif x == 6:
            console.print("Information of the Database", style="green1")
            console.print("-----#####----", style="red1")
            console.print(df.info(), style="sandy_brown")
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
            clm = eval(colored_input(
                f"{RED}Enter the column name in the list:", colorama.Fore.RED))
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
                f"{RED}Enter name of a Country / Countries in the form of like this -['India']:",   colorama.Fore.RED))
            for cnt in cntry:
                console.print(df.loc[df["Team"] == cnt, [
                    "Team", "Gold", "Silver", "Bronze"]])
                console.print("-----#####-----", style="red1")
        elif x == 11:
            menu()
            break


def operations():
    df = pd.read_csv("WCDSV.csv")
    ans = True
    while ans:
        console.print("-----Data Manipulation-----", style="green4")
        console.print("-----#####-----", style="red1")
        console.print(
            " [dark_sea_green]1.Inserting a Row[/] \n [sky_blue2]2.Deleting a Row[/] \n [pale_turquoise1]3.Inserting a column[/] \n [orchid]4.Deleting a column[/] \n [gold3]5.Renaming a column[/] \n [purple]6.Exit to Main Menu[/]")
        console.print("-----#####-----", style="red1")
        ans = int(colored_input(
            f"{RED}Enter Your Choice: ", colorama.Fore.RED))
        pd.set_option("display.max_columns", None)
        if ans == 1:
            console.print("Enter the colored_input in the Following Format")
            col = df.columns
            console.print(col)
            lst = eval(colored_input(
                f"{RED}Enter the row values in list: ", colorama.Fore.RED))
            sr = pd.Series(lst, index=col)
            row_df1 = pd.DataFrame([sr])
            df = pd.concat([row_df1, df], ignore_index=True)
            console.print(df)
            df.to_csv("WCDSV.csv", index=False)
            console.print("Row Added Successfully")
            console.print("----####----")
        elif ans == 2:
            inp = int(colored_input(
                f"{RED}Enter the row's index you want to delete: ", colorama.Fore.RED))
            df1 = df.drop(inp, axis=0)
            df1.to_csv("WCDSV.csv", index=False)
            console.print("----####----")
            console.print(f"DataFrame after row index number {inp} is deleted")
            console.print("----####----")
            console.print(df1)
            console.print("----####----")
        elif ans == 3:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            clname = str(colored_input(
                f"Enter the Column Name : ", colorama.Fore.RED))
            inp = int(
                colored_input(f"{RED}Enter the Column index \n where you want to insert the column: ", colorama.Fore.RED))
            df.insert(inp, clname, "Nan")
            console.print(df)
            df.to_csv("WCDSV.csv", index=False)
            console.print("----####----")
        elif ans == 4:
            pd.set_option("display.width", 500)
            pd.set_option("display.max_columns", None)
            console.print("DataFrame before deleting the column")
            console.print(df)
            inp = colored_input(
                f"{RED}Enter the column name you want to delete: ", colorama.Fore.RED)
            df = df.drop(inp, axis=1)
            console.print(f"DataFrame after deleting the column {inp} : ")
            console.print(df)
            df.to_csv("WCDSV.csv", index=False)
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
                colored_input(f"{RED}Enter the name of the column you want to change: ", colorama.Fore.GREEN))
            newcm = str(colored_input(
                f"{RED}Enter the new name of the column: ", colorama.Fore.GREEN))
            df = df.rename(columns={oldcm: newcm})
            console.print("-----#####-----", style="red1")
            console.print("DataFrame after changing the column name's")
            console.print("-----#####-----", style="red1")
            console.print(df)
            df.to_csv("WCDSV.csv", index=False)
            console.print("----#####-----", style="red1")
        elif ans == 6:
            console.print(
                "Sending command to the command center >>>>> Done !!!")
            menu()


menu()
