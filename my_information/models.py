from django.db import models


class AboutMeManager(models.Manager):
    def get_active_user(self):
        return self.get_queryset().filter(is_used=True).first()


class MyInformation(models.Model):
    FREELANCE_TYPE = (
        ('available', 'Available'),
        ('not available', 'Not Available')
    )
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField()
    about_me_text = models.TextField(verbose_name='About Me')
    residence = models.CharField(max_length=1500)
    address = models.CharField(max_length=2000)
    email = models.EmailField(max_length=2000)
    phone = models.CharField(max_length=400)
    image = models.ImageField(upload_to='user/')
    freelance = models.CharField(max_length=300, choices=FREELANCE_TYPE)
    is_used = models.BooleanField(default=True)
    copy_right = models.CharField(max_length=2000, null=True, blank=True)
    objects = AboutMeManager()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About You'

    def __str__(self):
        return self.name


class MyCategorySkills(models.Model):
    category_name = models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'CategorySkill'
        verbose_name_plural = 'CategorySkills'

    def __str__(self):
        return self.category_name


class MySkills(models.Model):
    MUCH_TYPE = (
        ('3', '50'),
        ('8', '75'),
        ('9', '100'),

    )
    user = models.ForeignKey(MyInformation, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=2000)
    skill_much = models.CharField(max_length=200, choices=MUCH_TYPE)
    category_skill = models.ForeignKey(MyCategorySkills, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill_name


class MyServices(models.Model):
    user = models.ForeignKey(MyInformation, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=300)
    service_about = models.TextField()
    service_image = models.ImageField(upload_to='services')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_name


class MyTag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class MyProjectsWork(models.Model):
    title = models.CharField(max_length=200, verbose_name='Project Name')
    blog_text = models.TextField(verbose_name='Project Description')
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs/', verbose_name='Project Image')
    user = models.ForeignKey(MyInformation, on_delete=models.CASCADE)
    tag = models.ManyToManyField(MyTag)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Contacts(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.full_name
