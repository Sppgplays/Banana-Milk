import api, coh, profit_loss, overheads
from gettext import find
from hashlib import new
from pathlib import Path
import re, csv



file_path = Path.cwd()/"Summary Report.txt"
file_path.touch()

def main():

    forex = api.api_function()
    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)

main()

