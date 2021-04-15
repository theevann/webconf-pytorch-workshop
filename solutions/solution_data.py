from pathlib import Path
from PIL import Image


class AlienPredatorDataset(Dataset):
    def __init__(self, root, split):
        self.root = root
        self.split = split
        
        # Load and save all image paths
        self.img_instances = []
        
        for img_path in Path(root, split, "alien").glob("*.jpg"):
            self.img_instances.append((img_path, 0))
            
        for img_path in Path(root, split, "predator").glob("*.jpg"):
            self.img_instances.append((img_path, 1))
    
    
    def __len__(self):
        return len(self.img_instances)
    
    
    def __getitem__(self, index):
        path, target = self.img_instances[index]
        
        with open(path, 'rb') as f:
            img = Image.open(f).convert('RGB')
            
        return (img, target)