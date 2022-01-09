import pandas as pd
import zipfile

zp = zipfile.ZipFile('/data.zip')
zp.namelist()
