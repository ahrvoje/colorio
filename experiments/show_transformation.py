#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
from __future__ import print_function, division

import argparse
import os
import tempfile
import matplotlib.pyplot as plt

from dolfin import Mesh, FunctionSpace, Function
import numpy

import colorio
import meshio
import meshzoo


def _main():
    args = _parse_cmd_arguments()

    content = numpy.load(args.infile)

    data = content.item()['data']
    ref_steps = content.item()['ref_steps']

    # # plot statistics
    # axes0 = problem.get_ellipse_axes(alpha0).T.flatten()
    # plt.plot(axes0, label='axes lengths before')
    # axes1 = problem.get_ellipse_axes(out.x).T.flatten()
    # plt.plot(axes1, label='axes lengths opt')
    # plt.legend()
    # plt.grid()

    # Plot unperturbed MacAdam
    # colorio.plot_luo_rigg(
    #     ellipse_scaling=1,
    colorio.save_macadam(
        'macadam-native.png',
        ellipse_scaling=10,
        plot_rgb_triangle=False,
        mesh_ref_steps=ref_steps,
        )

    points, cells = meshzoo.triangle(
        corners=numpy.array([
            [0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]
            ]),
        ref_steps=ref_steps
        )

    # https://bitbucket.org/fenics-project/dolfin/issues/845/initialize-mesh-from-vertices
    with tempfile.TemporaryDirectory() as temp_dir:
        tmp_filename = os.path.join(temp_dir, 'test.xml')
        meshio.write(
            tmp_filename, points, {'triangle': cells},
            file_format='dolfin-xml'
            )
        mesh = Mesh(tmp_filename)

    V = FunctionSpace(mesh, 'CG', 1)

    def get_u(alpha):
        n = V.dim()
        ax = alpha[:n]
        ay = alpha[n:]

        ux = Function(V)
        ux.vector().set_local(ax)
        ux.vector().apply('')

        uy = Function(V)
        uy.vector().set_local(ay)
        uy.vector().apply('')
        return ux, uy

    # Plot perturbed MacAdam
    def transform(XY, data=data):
        is_solo = len(XY.shape) == 1
        if is_solo:
            XY = numpy.array([XY]).T
        # print(XY)
        ux, uy = get_u(data)
        out = numpy.array([
            [ux(x, y) for x, y in XY.T],
            [uy(x, y) for x, y in XY.T],
            ])
        if is_solo:
            out = out[..., 0]
        return out

    # colorio.plot_luo_rigg(
    #     ellipse_scaling=1,
    plt.figure()
    colorio.plot_macadam(
        ellipse_scaling=10,
        # xy_to_2d=problem.pade2d.eval,
        xy_to_2d=transform,
        plot_rgb_triangle=False,
        mesh_ref_steps=ref_steps,
        )
    plt.xlim(-0.2, 0.9)
    plt.ylim(+0.0, 0.7)
    plt.savefig('macadam-{}.png'.format(ref_steps))
    return


def _parse_cmd_arguments():
    parser = argparse.ArgumentParser(
        description='Show piecewise linear transformation.'
        )
    parser.add_argument(
        'infile',
        help='input data file'
        )
    return parser.parse_args()


if __name__ == '__main__':
    _main()