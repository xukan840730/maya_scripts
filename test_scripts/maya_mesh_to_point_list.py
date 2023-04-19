import maya.OpenMaya as om


def mesh_to_point_list_os(in_mesh):
    # create empty point array
    mesh_point_array = om.MPointArray()

    # create function set and get points in object space
    in_mesh.getPoints(mesh_point_array, om.MSpace.kObject)

    # put each point to a list
    point_list = []
    for i in range(mesh_point_array.length()):
        point_list.append([mesh_point_array[i][0], mesh_point_array[i][1], mesh_point_array[i][2]])
    return point_list


def particleFillSelection():
    # get the active selection
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection)
    iterSel = om.MItSelectionList(selection, om.MFn.kMesh)
    iter_xfms = om.MItSelectionList(selection, om.MFn.kTransform)

    while not iter_xfms.isDone():
        dag_path = om.MDagPath()
        iter_xfms.getDagPath(dag_path)
        mfn_xfm = om.MFnTransform(dag_path)
        t = mfn_xfm.getTranslation(om.MSpace.kWorld)
        print(t.x, t.y, t.z)
        euler_rot = om.MEulerRotation()
        mfn_xfm.getRotation(euler_rot)
        print(euler_rot.x, euler_rot.y, euler_rot.z)
        iter_xfms.next()

    # go through selection
    while not iterSel.isDone():
        dagPath = om.MDagPath()
        iterSel.getDagPath(dagPath)
        currentInMeshMFnMesh = om.MFnMesh(dagPath)
        # test_xfm = om.MFnTransform(dagPath)
        return mesh_to_point_list_os(currentInMeshMFnMesh)


point_list = particleFillSelection()
