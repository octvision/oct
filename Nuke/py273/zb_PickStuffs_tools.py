"""
__title__ = zb_PickStuffs_tools.py
__author__ = zhangben 
__mtime__ = 2019/3/8 : 18:02
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import os, re, sys
import subprocess
import nuke
def modifyReadNode(eaRd, targDir, allFrms):
    """
    #copy 指定的read node 的 指定帧数的 素材 到 目标目录 修改read节点的 素材属性值
    :param eaRd: read node
    :param targDir: destination directory
    :param allFrms: specify want frams
    :return:
    """
#targDir = copy2Dri
    warnMesg = "The Following stuff not exist:"
    src_stuff = eaRd['file'].getValue()
    #src_stuff = r'//192.168.80.221/Images/MSS/sc15/sh01/chenshuh/MSS_sc15_sh01_LG_DY_15_L_v301/masterLayer/sc15_camL_L/beauty/sc15_camL_L.%04d.exr'
    #src_stuff2 = r"M:/COMP/MSS/DY/render/sc15/MSS_sc15_sh01_LG_DY_bg_A_v309/masterLayer/sc15_camL_L/beauty/sc15_camL_L.%04d.exr"
    #src_stuff3 = r"M:/COMP/CDFKBS/DY/render/SC05_sh01/CDFKBS_sc05_sh01_lg_DY_lgt_v013_0213_waifa/CDFKBS_sc05_sh01_lg_DY_lgt_v013_0213_waifa/masterLayer/cameraL/ID_shitou/cameraL.ID_shitou.%04d.png"
    #idex = sc_foder_index[-1]
    #rpl_folder = "/".join(dir_splt[:idex+1])
    src_stuff_splpth = os.path.split(src_stuff)
    cmp_stf_path = compile_path2(src_stuff)
    new_stuff_path =  "{}{}".format(targDir,cmp_stf_path['makeDir'])
    new_stuff_value = "{}{}/{}".format(targDir,cmp_stf_path['makeDir'],src_stuff_splpth[-1])
    print new_stuff_path
    print new_stuff_value
    stuff_name_spl = []
    stuff_name_spl_tmp = src_stuff_splpth[1].split('.')
    connector = '.'
    if len(stuff_name_spl_tmp) == 3:
        stuff_name_spl.extend(stuff_name_spl_tmp)
    else:
        connector = "_"
        # stuff_name_spl_tmp.append(stuff_name_spl_tmp)
        stuff_name_spl2 = stuff_name_spl_tmp[0].split('_')
        stuff_name_spl.append("_".join(stuff_name_spl2[:-1]))
        stuff_name_spl.append(stuff_name_spl2[-1])
        stuff_name_spl.append(stuff_name_spl_tmp[-1])
    copy2Dir=None
    for ea_frm in allFrms:
        #ea_frm = allFrms[2]
        singleStfnm = "{}{}{}.{}".format(stuff_name_spl[0], connector, stuff_name_spl[1]%(ea_frm), stuff_name_spl[2])
        print singleStfnm
        src_stfnm_full = os.path.normpath(os.path.join(src_stuff_splpth[0], singleStfnm))
        # src_stfnm_full = os.path.join(r"\\192.168.80.224\Images\CDMSS\sc04\sh01\yanglei1\CDMSS_sc04_sh01_xy_color_CH_v01_fx\masterLayer\CDMSS_sc04_sh01_an_c001_cam4L\crypto_material",singleStfnm)
        new_stf_full = os.path.normpath(os.path.join(new_stuff_path, singleStfnm))
        if not os.path.isfile(src_stfnm_full) :
            #or os.path.isfile(new_stf_full): continue
            print("there is not a stuff named :{} in the source directory\n{}".format(singleStfnm,src_stuff_splpth[0]))
            continue
        #
        copy2Dir = os.path.normpath(new_stuff_path)
        if not os.path.isdir(copy2Dir): os.makedirs(copy2Dir)
        p = subprocess.Popen(["copy", src_stfnm_full, copy2Dir], shell=True)
        p.wait()
        checkPath = re.sub("\\\\",'/',new_stf_full)
        if not os.path.isfile(checkPath):
            print("file copped FAILED ------------{}".format(checkPath))
        else:
            print("file copyed frome :{}  \nto   \n{}".format(src_stfnm_full,new_stf_full))
    if not os.path.isdir(copy2Dir):
        print("!!!!!!!!!copyed Fialed!!!!!!!!!!!!!!!!!!!!")
        warnMesg += "node :{}   needs  stuffs {}".format(eaRd.name(),os.linesep)
    else:
        print("why")
        eaRd['file'].setValue(new_stuff_value)
        print("value reset")
        eaRd['on_error'].setValue('checkerboard')
        print("set if missing  of node {}".format(eaRd.name()))
    if warnMesg != "The Following stuff not exist:": return warnMesg
    else: return None

def compile_path(src_stuff):
    """
    :param src_stuff: stuffs path
    :return: a dictionary , include two elements : the target path  and replace path strings
    """
    #src_stuff = src_stuff_splpth
    src_stuff_splpth = os.path.split(src_stuff)
    stuf_dir = src_stuff_splpth[0]
    dir_splt = stuf_dir.split('/')
    """
    because the directory of stuffs are very complicated, mainly for the  following there cases ,i use regular expression filter the folders that
    need to maintain the folder levels 
    # src_stuff = r'//192.168.80.221/Images/MSS/sc15/sh01/chenshuh/MSS_sc15_sh01_LG_DY_15_L_v301/masterLayer/sc15_camL_L/beauty/sc15_camL_L.%04d.exr'
    # src_stuff2 = r"M:/COMP/MSS/DY/render/sc15/MSS_sc15_sh01_LG_DY_bg_A_v309/masterLayer/sc15_camL_L/beauty/sc15_camL_L.%04d.exr"
    # src_stuff3 = r"M:/COMP/CDFKBS/DY/render/SC05_sh01/CDFKBS_sc05_sh01_lg_DY_lgt_v013_0213_waifa/CDFKBS_sc05_sh01_lg_DY_lgt_v013_0213_waifa/masterLayer/cameraL/ID_shitou/cameraL.ID_shitou.%04d.png"
    # idex = sc_foder_index[-1]
    #ea_folder = 'sc15'
    #ea_folder = 'sc15_camL_L'
    #ea_folder = 'SC05_sh01'
    """
    sc_folder_lst = []
    index = 0
    for ea_folder in dir_splt:
        if re.search('^(sc\d+)',ea_folder,re.I):
            print("now check {}".format(ea_folder))
            sc_fd_nm = re.search('^(sc\d+)',ea_folder,re.I).group()
            if not re.search("[^{}]\w+\d+".format(sc_fd_nm),ea_folder,re.I):
                if not re.search("[^{}]+".format(sc_fd_nm),ea_folder,re.I):
                    sc_folder_lst.append(ea_folder)
                    id = dir_splt.index(ea_folder)
                    index = id
                    if re.search('^(sh)\d+',dir_splt[id+1],re.I):
                        sc_folder_lst.extend(dir_splt[(id+1):(id+3)])
                        index = id+3
            else:
                sc_folder_lst.append(ea_folder)
                index = dir_splt.index(ea_folder)

    rpl_dir = "/".join(dir_splt[:index+1])
    mk_dir =  "/".join(dir_splt[index+1:])
    return {'replace_dir':rpl_dir,'makeDir':mk_dir}

def getPrjName(stufPathSpl):
    OCTV_PROJS_PATH = r"\\octvision.com\CG\Themes"
    PROJS = os.listdir(OCTV_PROJS_PATH)
    intItem = set(PROJS) & set(stufPathSpl)
    if intItem: return list(intItem)[0]
    else: return None
def compile_path2(src_stuff):
    src_stuff_spl = os.path.split(src_stuff)
    stuf_dir = src_stuff_spl[0]
    stufPathSpl = stuf_dir.split('/')
    PRJName = getPrjName(stufPathSpl)
    if not PRJName:
        return compile_path(src_stuff)
    index = stufPathSpl.index(PRJName)
    rpl_dir = "/".join(stufPathSpl[:index])
    mk_dir =  "/".join(stufPathSpl[index:])
    return {'replace_dir':rpl_dir,'makeDir':mk_dir}
def _createPannel():# panel
    panel = nuke.Panel('PickStuffs_v01')
    panel.addFilenameSearch('destination', '/tmp')
    panel.addSingleLineInput('frames', '{}-{}'.format(nuke.root().firstFrame(), nuke.root().lastFrame()))
    return panel, panel.show()
def pick_stuff_panel(): # 接受用户输入的 路径 和帧数，返回 帧数列表
    # if __name__ == "__main__":
    (p, ret) = _createPannel()
    # ==get all need frames
    if not ret: return None
    copy2Dri = p.value('destination')
    frms = p.value('frames')
    frm_splt_comma = frms.split(',')
    allFrms = []
    for ea in frm_splt_comma:
        if not re.search('-', ea) and ea not in allFrms:
            allFrms.append(int(ea))
        else:
            frm_rang = nuke.FrameRange(ea)
            for ea_frm in (range(frm_rang.first(), frm_rang.last()+1)):
                if ea_frm not in allFrms: allFrms.append(ea_frm)
    return {'dir':copy2Dri,'frms':allFrms}

def main():
    sel_reads = nuke.selectedNodes('Read')
    if len(sel_reads) == 0:
        nuke.message("You need to select at least one read node")
        return None
    ret = pick_stuff_panel()
    if not ret: return None
    copy2Dri = ret['dir']
    copy2Dri = re.sub("\\\\", '/', copy2Dri)
    copy2Dri = re.sub("/$", "", copy2Dri)
    copy2Dri = re.sub(".$", "{}/".format(re.search(".$", copy2Dri).group()), copy2Dri)
    allFrms = ret['frms']
    warningMesgs = []
    for eaRd in sel_reads:
        print ("Now start set read node ::{}".format(eaRd.name()))
        wmsg = modifyReadNode(eaRd, copy2Dri, allFrms)
        if wmsg: warningMesgs.append(wmsg)
    if len(warningMesgs) > 0:
        wmsg_str = " ".join(warningMesgs)
        nuke.message(wmsg_str)
if __name__ == "__main__":
    main()










