import subprocess
import pathlib
import os
import JSONHelper

if __name__ == '__main__':
    params = JSONHelper.read(
        "./Routines/Script/Parameters.json"
    )  # <-- read parameter file (contains dataset paths)

    dim = 32  # <-- dimension for CAD voxelization
    scene_name_list = os.listdir(params['shapenet'])

    for scene_name in scene_name_list:
        scene_folder_path = params['shapenet'] + scene_name + '/'
        if not os.path.exists(scene_folder_path):
            continue

        obj_name_list = os.listdir(scene_folder_path)

        for obj_name in obj_name_list:
            f = scene_folder_path + obj_name + '/models/model_normalized.obj'
            if not os.path.exists(f):
                continue

            print('running at', f)
            catid_cad = f.split("/", 6)[4]
            id_cad = f.split("/", 6)[5]

            outdir = params["shapenet_voxelized"] + "/" + catid_cad
            pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
            outfile_df = outdir + "/" + id_cad + "__0__.df"

            # -> voxelize as DF
            try:
                program = ["../DFGen/main", f, str(dim), "1", "1", outfile_df]
                print(" ".join(str(x) for x in program))
                subprocess.check_call(program)
            except subprocess.CalledProcessError:
                pass
            # <-

            # -> visualize as PLY file
            try:
                outfile_ply = outfile_df.rsplit(".", 1)[0] + ".ply"
                program = [
                    "../Vox2Mesh/main", "--in", outfile_df, "--out",
                    outfile_ply, "--is_unitless", "1"
                ]
                print(" ".join(str(x) for x in program))
                subprocess.check_call(program)
            except subprocess.CalledProcessError:
                pass
            # <-
