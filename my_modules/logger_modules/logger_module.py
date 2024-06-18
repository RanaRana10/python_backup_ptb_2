
'''
This module is for using the Logger
** "import setup_logger" for common msg which shows the bot has started default form PTB examples
** "import setup_file_logger" if we use this it will save my logger information into a file
    To use this: rana_logger = setup_file_logger()
** "import setup_console_logger" , if i want to use it i need to call it 
just ** import setup_file_logger ** and then
RanaUniverse_Logger = setup_file_logger()
RanaUniverse_Logger()
'''

import logging
from pathlib import Path


def setup_logger():
    '''this is basic to show if the bot has started or not'''
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger(__name__)




def create_log_file():
    log_folder = Path("RanaUniverse") / "Logger_files"
    log_folder.mkdir(parents=True, exist_ok=True)
    log_file = log_folder / "0 Rana LOG FIle.log"
    return log_file





def setup_file_logger():
    '''This is special logger to call to to save logger files into the file'''
    log_file = create_log_file()

    rana_logger = logging.getLogger("RANA NAME")
    rana_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("FILE is:%(asctime)s ---Name is %(name)s -- ***%(levelname)s*** - %(message)s")

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    rana_logger.addHandler(file_handler)
    rana_logger.propagate = False
    return rana_logger





def setup_console_logger():
    '''When i will call this this will work like simple print() statements'''
    terminal_logger = logging.getLogger("RANA UNIVERSE TERMINAL")
    terminal_logger.setLevel(logging.DEBUG)
    string_msg = ("CONSOLE is:%(asctime)s ---Name is %(name)s -- ***%(levelname)s*** - %(message)s")
    formatter = logging.Formatter(string_msg)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    terminal_logger.addHandler(console_handler)
    terminal_logger.propagate = False
    return terminal_logger








