from __future__ import unicode_literals

import uuid

from django.db import models

from inchi.identifier import InChIKey

class Inchi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.IntegerField(db_column='version_id')
    block1 = models.CharField(max_length=14, db_column='block1')
    block2 = models.CharField(max_length=10, db_column='block2')
    block3 = models.CharField(max_length=1, db_column='block3')
    key = models.CharField(max_length=27, db_column='key', blank=True, null=True)
    string = models.CharField(max_length=32768, blank=True, null=True)



    class Meta:
        unique_together = ('block1', 'block2', 'block3', 'version')

    def add_key(self, inchikey, *args, **kwargs):
        self.block1, self.block2, self.block3 = inchikey.blocks
        self.key = inchikey.element['well_formatted_no_prefix']
        self.version = inchikey.element['version']
        super(Inchi, self).save(*args, **kwargs)

    def add_string(self, inchi, *args, **kwargs):
        self.string = inchi.element['well_formatted']
        self.version = inchi.element['version']
        super(Inchi, self).save(*args, **kwargs)

    def add_key_and_string(self, inchikey, inchistring, *args, **kwargs):
        self.block1, self.block2, self.block3 = inchikey.blocks
        self.key = inchikey.element['well_formatted_no_prefix']
        self.string = inchistring.element['well_formatted']
        self.version = inchikey.element['version']
        super(Inchi, self).save(*args, **kwargs)


    @property
    def __str__(self):
        inchikey = InChIKey(block1=self.block1, block2=self.block2, block3=self.block3)
        return inchikey.element['well_formatted_no_prefix']


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(unique=True, max_length=32768, blank=True, null=True)
    abbreviation  = models.CharField(max_length=32, blank=True, null=True)
    url = models.URLField(max_length=4096, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', blank=True, null=True)
    organization = models.ForeignKey('Organization', blank=True, null=True)
    name = models.CharField(max_length=32768, blank=True, null=True)
    group = models.CharField(max_length=32768, blank=True, null=True)
    contact = models.CharField(max_length=32768, blank=True, null=True)
    url = models.URLField(max_length=4096, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('parent', 'organization', 'name', 'group', 'contact')

    def __str__(self):
        return "%s[%s, %s]" % (self.name, self.group, self.contact)


class EntryPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    publisher = models.ForeignKey('Publisher')
    url = models.URLField(max_length=4096)
    description = models.TextField(max_length=32768, blank=True, null=True)

    class Meta:
        unique_together = ('publisher', 'url')

    def __str__(self):
        return "%s[%s]" % (self.publisher, self.url)
