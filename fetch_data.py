import os

import mdshare as md
from mdshare.mdshare import get_available_files_dict
from tqdm import tqdm

required_dataset_patterns = (
    'pentapeptide*',
    'alanine*',
    'hmm-doublewell-2d-100k.npz',
)
outdir = 'notebooks/data'
os.makedirs(outdir, exist_ok=True)
repository = ('ftp.imp.fu-berlin.de', 'pub/cmb-data/')
sizes = get_available_files_dict(repository)
to_download = []

for f in required_dataset_patterns:
    to_download.append(md.search(f))

total = sum(int(sizes[f]['size']) for dataset in to_download for f in dataset)

bar = tqdm(desc='Fetching data', total=total, unit='bytes', unit_scale=True)
for dataset in to_download:
    for f in dataset:
        s = int(sizes[f]['size'])
        md.fetch(f, working_directory=outdir)
        bar.update(s)
