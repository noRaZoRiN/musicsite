from datetime import date


from django.db import models


class Category(models.Model):
    """КАТЕГОРИЯ"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Singer(models.Model):
    """ПЕВЦЫ"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="singers/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Genre(models.Model):
    """ЖАНРЫ"""
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Song(models.Model):
    """ПЕСНЯ"""
    objects = None
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default="")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="songs/")
    year = models.PositiveIntegerField("Дата выхода", default=2025)
    country = models.CharField("Страна", max_length=30)
    singer = models.ManyToManyField(Singer, verbose_name="Исполнители")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    premiere = models.DateField("Дата премьеры", default=date.today)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    audio_file = models.FileField(upload_to='songs/', verbose_name="музыка", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class SongShorts(models.Model):
    "ОТРЫВОК ИЗ ПЕСНИ"
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="SongShorts")
    song = models.ForeignKey(Song, verbose_name="Песня", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отрывок"
        verbose_name_plural = "Отрывки"

class RatingStar(models.Model):
    "ЗВЕЗДА РЕЙТИНГА"
    value = models.PositiveIntegerField("Оценка", default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"


class Rating(models.Model):
    """РЕЙТИНГ"""
    ip = models.GenericIPAddressField("IP адрес")
    star = models.ForeignKey("RatingStar", on_delete=models.CASCADE, verbose_name="Звезда")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Песня")

    def __str__(self):
        return f"{self.star} - {self.song}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """ОТЗЫВЫ"""

class Review(models.Model):
    username = models.CharField(max_length=255, default='default_user')
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    song = models.ForeignKey("Song", on_delete=models.CASCADE, verbose_name="Песня")

    def __str__(self):
        return f"{self.username} - {self.song}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Songlist(models.Model):
    audio_file = models.FileField(upload_to='uploads/')