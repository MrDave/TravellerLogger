from django.db import models
from django.contrib.auth.models import User


class GameDate(models.Model):
    year = models.IntegerField()
    day_of_the_year = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["year", "day_of_the_year"], name="unique_date"),
            models.CheckConstraint(
                condition=models.Q(day_of_the_year__gte=1) & models.Q(day_of_the_year__lte=365),
                name="days_range_constraint",
                violation_error_message="days must be in range 1-365",
            ),
        ]
        ordering = ["year", "day_of_the_year"]

    def __str__(self):
        return f"{self.day_of_the_year:03d}-{self.year} IC"


class Campaign(models.Model):
    owner = models.ForeignKey(User, related_name="campaigns", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    current_date = models.ForeignKey(GameDate, related_name="campaigns", on_delete=models.PROTECT)

    class Meta:
        ordering = ["owner", "name"]

    def __str__(self):
        return self.name


class LogEntry(models.Model):
    campaign = models.ForeignKey(Campaign, related_name="log_entries", on_delete=models.CASCADE)
    game_date = models.ForeignKey(GameDate, related_name="log_entries", on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["campaign", "game_date"],
                name="unique_log_for_date",
            )
        ]

    def __str__(self):
        return f"{self.campaign} - {self.game_date}"

