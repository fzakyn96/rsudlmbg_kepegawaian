# -*- coding: utf-8 -*-

from odoo import models, fields

class rsudlmbg_golongan(models.Model):
    _name = 'rsudlmbg.golongan'
    _description = 'rsudlmbg.golongan'

    golongan = fields.Char(string="Golongan")
    detail_golongan = fields.Char(string="Detail Golongan")

class rsudlmbg_jabatan(models.Model):
    _name = 'rsudlmbg.jabatan'
    _description = 'rsudlmbg.jabatan'

    urutan = fields.Integer(string="Urutan")
    jabatan = fields.Char(string="Jabatan")

class rsudlmbg_pendidikan(models.Model):
    _name = 'rsudlmbg.pendidikan'
    _description = 'rsudlmbg.pendidikan'

    akronim_pendidikan = fields.Char(string="Akronim")
    pendidikan = fields.Char(string="Pendidikan")

class rsudlmbg_tipe_pegawai(models.Model):
    _name = 'rsudlmbg.tipe.pegawai'
    _description = 'rsudlmbg.tipe.pegawai'

    akronim_tipe_pegawai = fields.Char(string="Akronim")
    tipe_pegawai = fields.Char(string="Tipe Pegawai")

class rsudlmbg_jenis_kelamin(models.Model):
    _name = 'rsudlmbg.jenis.kelamin'
    _description = 'rsudlmbg.jenis.kelamin'

    akronim_jenis_kelamin = fields.Char(string="Akronim")
    jenis_kelamin = fields.Char(string="Jenis Kelamin")
