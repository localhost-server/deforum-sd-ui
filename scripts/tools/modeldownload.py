# This file is part of sygil-webui (https://github.com/Sygil-Dev/sygil-webui/).

# Copyright 2022 Sygil-Dev team.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
import os
import os.path as op

def dnldModels():
    if op.exists('models/model.ckpt'):
        pass
    else:
        os.system('curl -L https://huggingface.co/kaliansh/sdfull/resolve/main/v1-5-pruned-emaonly.ckpt -o models/model.ckpt')
        
    if op.exists('models/dpt_large-midas-2f21e586.pt'):
        pass
    else:
        os.system('curl -L https://github.com/intel-isl/DPT/releases/download/1_0/dpt_large-midas-2f21e586.pt -o models/dpt_large-midas-2f21e586.pt')
        
    if op.exists('pretrained/AdaBins_nyu.pt'):
        pass
    else:
        os.mkdir('pretrained')
        os.system('curl -L https://cloudflare-ipfs.com/ipfs/Qmd2mMnDLWePKmgfS8m6ntAg4nhV5VkUyAydYBp8cWWeB7/AdaBins_nyu.pt -o pretrained/AdaBins_nyu.pt')
        
    if op.exists('src/realesrgan/experiments/pretrained_models/RealESRGAN_x4plus.pth') and op.exists('src/realesrgan/experiments/pretrained_models/RealESRGAN_x4plus_anime_6B.pth'):
        pass
    else:
        os.system('curl -L https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -o src/realesrgan/experiments/pretrained_models/RealESRGAN_x4plus.pth')
        os.system('curl -L https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth -o src/realesrgan/experiments/pretrained_models/RealESRGAN_x4plus_anime_6B.pth')
    
    if op.exists('src/gfpgan/experiments/pretrained_models/GFPGANv1.4.pth'):
        pass 
    else:
        os.system('curl -L https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth -o src/gfpgan/experiments/pretrained_models/GFPGANv1.4.pth')
    