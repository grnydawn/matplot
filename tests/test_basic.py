from microapp import MicroappProject

import os

here = os.path.dirname(os.path.abspath(__file__))
outimg = os.path.join(here, "image.png")
#unzipped = os.path.join(here, "data")

def test_basic():

    prj = MicroappProject()
    data = "@[1,2,4,3]"
    cmd = "matplot %s -o @<'\"%s\"'> --noshow" % (data, outimg )

    ret = prj.main(cmd)

    assert ret == 0
    assert os.path.exists(outimg)

    os.remove(outimg)


def test_title():

    prj = MicroappProject()
    data = "@[1,2,4,3]"
    cmd = "matplot %s --title 'ax:My figure' -o %s --noshow" % (data, outimg )


    ret = prj.main(cmd)

    assert ret == 0
    assert os.path.exists(outimg)

    os.remove(outimg)
