"""pyloco netcdf module
"""

from __future__ import unicode_literals

import os
import pyloco

here, myname = os.path.split(__file__)
#datadir = os.path.join(here, "data")
#rootdir = os.path.realpath(os.path.join(here, ".."))
#matplot = os.path.join(rootdir, "nctools", "plot", "matplot", "matplot.py")
matplot = "matplot.py"
#imgfile = os.path.join(datadir, "img.png")
imgfile = "img.png"

class TaskMatplotTests(pyloco.TestCase):

    def __init__(self, *vargs, **kwargs):

        super(TaskMatplotTests, self).__init__(*vargs, **kwargs)

        self.argv = [
            "--debug",
            "--noshow",
            "--save", "'%s'" % imgfile
        ]
            #"--backend", "WebAgg",

    def setUp(self):

        if os.path.exists(imgfile):
            os.remove(imgfile)

    def tearDown(self):

        #import pdb; pdb.set_trace()
        if os.path.exists(imgfile):
            os.remove(imgfile)

    def _default_assert(self, retval):

        self.assertEqual(retval, 0)
        self.assertTrue(os.path.exists(imgfile))

    def test_figure(self):

        argv = self.argv + [
            "--figure", "'test'@suptitle",
        ]

        retval, forward = self.perform_test(matplot, argv=argv)

        self._default_assert(retval)

    def test_title(self):

        argv = self.argv + [
            "--title", "'test'",
            "--plot", "[3,1,2]",
        ]

        retval, forward = self.perform_test(matplot, argv=argv)

        #import pdb; pdb.set_trace()
        self._default_assert(retval)

    def test_bar(self):

        argv = self.argv + [
            "--title", "'test'",
            "--plot", "[0,1,2], [3,1,2]@bar",
        ]

        retval, forward = self.perform_test(matplot, argv=argv)

        #import pdb; pdb.set_trace()
        self._default_assert(retval)

    def test_ticks(self):

        argv = self.argv + [
            "--title", "'test'",
            "--plot", "[0,1,2], [3,1,2]@bar",
            "--xaxis", "[0,1,2]@ticks",
            "--xaxis", "['A', 'B', 'C']@ticklabels",
        ]

        retval, forward = self.perform_test(matplot, argv=argv)

        #import pdb; pdb.set_trace()
        self._default_assert(retval)

    def test_clone(self):

            #"--multiproc", "2,spawn",
        argv = [
            "--log", "clonetest.log",
            "--multiproc", "2",
            "--clone", "[1,2,3],[3,5,2]"
        ]

        newargv = list(self.argv)
        idx = newargv.index("--save")
        newargv.pop(idx+1)
        newargv.pop(idx)
        subargv = [matplot] + newargv + [
            "--save", "'%d.png'%_pathid_",
        ]

        retval, forward = self.perform_test("", argv=argv, subargv=subargv)

        self.assertEqual(retval, 0)
        self.assertTrue(os.path.exists("0.png"))
        os.remove("0.png")
        self.assertTrue(os.path.exists("1.png"))
        os.remove("1.png")

    def test_legend(self):

        argv = self.argv + [
            "--title", "'test'",
            "--plot", "[0,1,2], label='PlotA'",
            "--plot", "[3,1,2], label='PlotB'",
            "-l",
        ]

        retval, forward = self.perform_test(matplot, argv=argv)

        #import pdb; pdb.set_trace()
        self._default_assert(retval)


    def tttest_pickle(self):

        picklefile = os.path.join(datadir, "test.ppf")

        argv = self.argv + [
            "--read-pickle", picklefile,
            "--subplot", "111@ax",
            "--plot", "_{data[0]['dims']['lat']['variable']['data'][:]:arg}_@plot",
        ]

        retval, forward = self.perform_test(matplot, argv=argv)

        self._default_assert(retval)

        #self.assertIn("data", forward)
        #self.assertEqual(forward["data"], ['lat', 'lon', 'bnds', 'plev', 'time'])


#test_classes = (TaskMatplotTests,)
