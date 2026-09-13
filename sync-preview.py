from pathlib import Path
import shutil
root=Path(__file__).resolve().parent;out=root/'dist';out.mkdir(exist_ok=True)
for p in root.iterdir():
 if p.is_file() and (p.suffix in ['.html','.css','.js','.pdf'] or p.name in ['robots.txt','sitemap.xml']):shutil.copy(p,out/p.name)
for name in ['images','fonts','ventures','company','government-contracting','contact']:
 shutil.copytree(root/name,out/name,dirs_exist_ok=True)
print('Synced static review bundle')
