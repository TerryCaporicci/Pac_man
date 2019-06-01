from django.db import models


class scoreboard(models.Model):
    pseudo = models.CharField(max_length=15)
    score = models.IntegerField(null=False)
    country = models.TextField(null=True)
    # time = models.TimeField( auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "scoreboard"
        ordering = ['score']

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre
